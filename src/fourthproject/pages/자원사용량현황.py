import time
import requests
import streamlit as st
import pandas as pd

# Prometheus 서버 URL
PROMETHEUS_URL = "http://localhost:9090"

# Prometheus에서 메트릭을 쿼리하는 함수
def query_prometheus(query):
    # 쿼리를 URL 파라미터로 Prometheus API 호출
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query})
    
    if response.status_code == 200:
        result = response.json()['data']['result']
        if result:
            return float(result[0]['value'][1])  # 첫 번째 결과의 값 반환
    else:
        st.error(f"프로메테우스 서버로 데이터를 가져오는데 실패했습니다. 응답 코드: {response.status_code}")
        return None

# Streamlit 대시보드 설정
st.title("Real-Time System Metrics Dashboard")

# 실시간 업데이트용 빈 공간 - 여기에 차트가 계속 불러와지는 느낌
st.header("CPU 사용량 그래프")
cpu_placeholder = st.empty()
#st.header("메모리 사용량 그래프")
#memory_placeholder = st.empty()
st.header("네트워크 대역폭 사용량 그래프 (100MB/s 기준)")
network_placeholder = st.empty()

# 데이터 리스트
#cpu_data, memory_data, network_data, time_data = [], [], [], []
cpu_data, network_data, time_data = [], [], []

# 주기적으로 metric을 갱신하는 함수
def collect_metrics():
    while True:
        # 현재 시각 추가
        current_time = pd.Timestamp.now()
        time_data.append(current_time)

        # CPU 사용률 쿼리
        cpu_query = 'rate(process_cpu_seconds_total[1m]) * 100'
        cpu_usage = query_prometheus(cpu_query)
        if cpu_usage is not None:
            cpu_data.append(cpu_usage)

        # 메모리 사용률 쿼리
       # memory_query = '(process_virtual_memory_bytes / process_virtual_memory_max_bytes) * 100'
       # memory_usage = query_prometheus(memory_query)
       # if memory_usage is not None:
       #     memory_data.append(memory_usage)

        # 네트워크 대역폭 사용률 계산
        network_query = '(rate(process_network_receive_bytes_total[1m]) + rate(process_network_transmit_bytes_total[1m])) / (100 * 1024 * 1024) * 100'
        network_usage = query_prometheus(network_query)
        if network_usage is not None:
            network_data.append(network_usage)

        # 데이터프레임 생성
        data = {
            "Time": time_data,
            "CPU Usage (%)": cpu_data,
        #    "Memory Usage (%)": memory_data,
            "Network Bandwidth Usage (%)": network_data
        }
        df = pd.DataFrame(data)

        # 실시간 차트 업데이트
        with cpu_placeholder.container():
            st.line_chart(df, x="Time", y="CPU Usage (%)", use_container_width=True)

        #with memory_placeholder.container():
        #    st.line_chart(df, x="Time", y="Memory Usage (%)", use_container_width=True)

        with network_placeholder.container():
            st.line_chart(df, x="Time", y="Network Bandwidth Usage (%)", use_container_width=True)

        time.sleep(1)  # 1초마다 갱신

if __name__ == "__main__":
    print("시스템의 사용량관련 metric 수집을 시작합니다...")
    collect_metrics()

