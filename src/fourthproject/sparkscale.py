import subprocess
import json
import yaml
import time
import os
import pytz
from datetime import datetime
import requests
import sys

timezone = pytz.timezone("Asia/Seoul")
file_path = __file__
directory = os.path.dirname(file_path)
yml_path = os.path.join(directory, "spark/docker-compose.yml")
log_path = os.path.join(directory, "dockerlog.log")
if not os.path.exists(directory):
   os.makedirs(directory)

# 로그 파일 있는지 체크 없으면 칼럼 넣은 파일 생성 있으면 데이터 입력
if not os.path.exists(log_path):
    with open(log_path, "w") as f:
        f.write("time,CPUuses,scaleIO\n")
# scale in/out 수동 조작을 위한 함수
def scalein(num):
    log_path = wherelog()
    blogcount = subprocess.check_output(["bash", "-c", "docker stats --no-stream | grep spark-spark-worker | wc -l"])
    blogcountj = int(blogcount.decode("utf-8").strip())
    local_time = datetime.now(timezone)
    formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    cntdocker = blogcountj - int(num)
    _, result2 = checkCPU(blogcountj)
    subprocess.run(['docker', 'compose', '-f', f'{yml_path}','up', '-d', '--scale', f'spark-worker={cntdocker}'])
    with open(log_path, "a", encoding="utf-8", newline='') as f:
        f.write(f"{formatted_time},{result2},I\n")

def scaleout(num):
    log_path = wherelog()
    blogcount = subprocess.check_output(["bash", "-c", "docker stats --no-stream | grep spark-spark-worker | wc -l"])
    blogcountj = int(blogcount.decode("utf-8").strip())
    local_time = datetime.now(timezone)
    formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    _, result2 = checkCPU(blogcountj)
    cntdocker = blogcountj + int(num)
    subprocess.run(['docker', 'compose', '-f', f'{yml_path}','up', '-d', '--scale', f'spark-worker={cntdocker}'])
    with open(log_path, "a", encoding="utf-8", newline='') as f:
        f.write(f"{formatted_time},{result2},O\n")


def checkCPU(num):
    CPUchecklist = []
    statusCPU = "stable"
    for i in range(1, num + 1):
        r = subprocess.check_output(["docker", "stats", f"spark-spark-worker-{i}", "--no-stream", "--format", "{{json .}}"])
        j = json.loads(r.decode("utf-8"))
        CPUchecklist.append(float(j['CPUPerc'].strip('%')))

    return CPUchecklist, round(sum(CPUchecklist), 2)

def checkAll():
    blogcount = subprocess.check_output(["bash", "-c", "docker stats --no-stream | grep spark-spark-worker | wc -l"])
    blogcountj = int(blogcount.decode("utf-8").strip())
    local_time = datetime.now(timezone)
    formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    result1, result2 = checkCPU(blogcountj)
    return formatted_time, blogcountj, result2

def wherelog():
    file_path = __file__
    directory = os.path.dirname(file_path)
    log_path = os.path.join(directory, "dockerlog.log")
    # print(f"패키지 설치된 위치: {directory}")
    # print(f"log 저장되는 곳 : {log_path}")
    return log_path

