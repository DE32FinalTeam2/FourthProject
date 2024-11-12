import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from k1s.autoscale import wherelog

st.set_page_config(
    page_title="scale in/out 관리자 페이지 3",
    page_icon="👋",
)

st.write("스케일 인 아웃 현황👋")

log_path=wherelog()

# if 문 안으로 전체 코드 이동
if os.path.exists(log_path):
    # CSV 파일을 읽어서 DataFrame 생성
    df = pd.read_csv(log_path)

    # 필요한 컬럼만 선택
    cdf = df[['time', 'CPUuses']]

    # 'scaleIO' 컬럼에 따라 데이터 분리
    Ispot = df[df['scaleIO'] == "I"]
    Ospot = df[df['scaleIO'] == "O"]
    
    st.write("scale in ")
    st.dataframe(Ispot)
    st.write("scale out")
    st.dataframe(Ospot)

else : 
    st.write("아직 로그가 없습니다.")

#if os.path.exists(log_path):
#df = pd.read_csv(log_path)
#cdf = df[['time','CPUuses']]
#Ispot = df[df['scaleIO']=="I"]
#Ospot = df[df['scaleIO']=="O"]
#st.dataframe(Ispot)
#st.dataframe(Ospot)
#st.write(df.columns)

#flg = plt.figure()
#plt.plot(df['time'],df['CPUuses'],data=df)
#plt.scatter(x=Ispot['time'], y=Ispot['CPUuses'],marker='o',color="red",label='scale in ')
#plt.scatter(x=Ospot['time'], y=Ospot['CPUuses'],marker='s',color="green",label='scale out')
#plt.legend(loc='lower left')

#plt.xticks(rotation=45)
#st.pyplot(flg)


