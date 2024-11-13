import streamlit as st
import pandas as pd
import os
import time
from fourthproject.autoscale import wherelog
import plotly.graph_objects as go

st.set_page_config(
    page_title="scale in/out 관리자 페이지 2",
    page_icon="👋",
)

st.subheader("도커 및 자원 사용량 현황👋")

# 로그 파일 경로 설정
log_path = wherelog()
print(log_path)

# 데이터 자동 업데이트를 위한 새로고침 주기 설정 (초 단위)
REFRESH_INTERVAL = 5  # 10초마다 새로고침

# Streamlit에서 업데이트된 그래프를 표시할 공간을 먼저 준비
graph_placeholder = st.empty()

while True:
    # 데이터가 있는 경우에만 그래프를 그리도록 조건 설정
    if os.path.exists(log_path):
        # CSV 파일을 읽어서 DataFrame 생성, 'time' 컬럼을 날짜 형식으로 변환
        df = pd.read_csv(log_path, parse_dates=['time'])

        # 필요한 컬럼만 선택
        cdf = df[['time', 'CPUuses']]

        # 'scaleIO' 컬럼에 따라 데이터 분리
        Ispot = df[df['scaleIO'] == "I"]
        Ospot = df[df['scaleIO'] == "O"]

        # Plotly 그래프 생성
        fig = go.Figure()

        # 선 그래프 추가 (CPU 사용량)
        fig.add_trace(go.Scatter(x=df['time'], y=df['CPUuses'], mode='lines', name='CPU 사용량'))

        # scale in 및 scale out 이벤트 표시
        fig.add_trace(go.Scatter(x=Ispot['time'], y=Ispot['CPUuses'], mode='markers', marker=dict(color='red', symbol='circle'), name='scale in'))
        fig.add_trace(go.Scatter(x=Ospot['time'], y=Ospot['CPUuses'], mode='markers', marker=dict(color='green', symbol='square'), name='scale out'))

        # x축 및 y축 레이블 설정
        fig.update_layout(
            xaxis_title="시간",
            yaxis_title="CPU 사용량 (%)",
            title="CPU 사용량 및 Scale In/Out 이벤트",
            xaxis=dict(rangeslider=dict(visible=True)),  # 드래그를 위한 범위 슬라이더 추가
            legend=dict(x=0, y=1, bgcolor="rgba(255, 255, 255, 0.5)")
        )

        # 고유한 key 생성: 현재 시간을 기반으로
        unique_key = f"unique_graph_key_{time.time()}"

        # 새로고침 없이 그래프만 업데이트, 고유한 key 추가
        graph_placeholder.plotly_chart(fig, use_container_width=True, key=unique_key)

    else:
        st.write("아직 로그가 없습니다.")

    # 설정한 주기마다 대기
    time.sleep(REFRESH_INTERVAL)

