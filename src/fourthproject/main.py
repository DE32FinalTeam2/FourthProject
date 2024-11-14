import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from fourthproject.sparkscale import checkAll,scalein,scaleout,wherelog

st.set_page_config(
    page_title="scale in/out 관리자 메인 페이지 ",
    page_icon="👋",
)

st.write("스케일 인/아웃 관리 페이지👋")

result0,result1,result2 = checkAll()

with st.form(key='my_form'):
    st.write("시간:",result0,"총 컨테이너 수:",result1, "CPU 총 사용량:",result2)

    col1, col2 = st.columns(2)
    with col1:
        log_button = st.form_submit_button(label='log path')
    with col2:
        rerun_button = st.form_submit_button(label='View Current Dockers')
    if log_button:
        st.write("log exist in ",wherelog())
    if rerun_button:
        st.write("Review Current Dockers")
        st.rerun()

with st.form(key="docker"):
    cnt = st.text_input("스케일 인/아웃할 컨테이너의 개수")
    
    col1,col2 =st.columns(2)
    with col1:
        scale_out = st.form_submit_button(label='manual scale out')
    with col2:
        scale_in = st.form_submit_button(label='manual scale in')
    if scale_out:
        result0,result1,result2 = checkAll()
        if (result1+int(cnt)) <5:
            scaleout(cnt)
            dockercnt=result1+int(cnt)
            st.write(cnt,"개","scale out 되었습니다.","총 컨테이너 수:",dockercnt,"개 입니다.")
        else :
            st.write("4개 이하만 생성 가능합니다.")
    if scale_in:
        result0,result1,result2 = checkAll()
        if result1 >1:
            scalein(cnt)
            dockercnt=result1-int(cnt)
            st.write(cnt,"개","scale out 되었습니다.","총 컨테이너 수:",dockercnt,"개 입니다.")
        else : 
            st.write("현재 운용중인 컨테이너가 1개로 이미 최소입니다.")
