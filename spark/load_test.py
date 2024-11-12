# load_test.py
from pyspark.sql import SparkSession
import time

# SparkSession 생성
spark = SparkSession.builder \
    .appName("LoadTest") \
    .master("spark://127.0.0.1:7077") \
    .getOrCreate()

# 부하 테스트 시작
start_time = time.time()
while time.time() - start_time < 60:  # 60초 동안 실행
    # 데이터 프레임 생성 및 간단한 연산 수행
    data = [(i, i * 2) for i in range(100000)]  # 큰 데이터 생성
    df = spark.createDataFrame(data, ["number", "double"])
    df.groupBy("number").count().collect()  # 집계 연산

# SparkSession 종료
spark.stop()

