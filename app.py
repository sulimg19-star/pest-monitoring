import streamlit as st
import pandas as pd
import datetime

# 앱 설정
st.set_page_config(page_title="수목 병해충 모니터링", layout="wide")

st.title("🌲 시민 참여형 수목 병해충 모니터링")
st.markdown("시민 여러분의 제보가 우리 숲을 건강하게 만듭니다.")

# 화면을 두 칸으로 나눕니다
col1, col2 = st.columns(2)

with col1:
    st.header("📍 발견 신고하기")
    # 폼 만들기
    with st.form("my_form", clear_on_submit=True):
        date = st.date_input("발견 날짜", datetime.date.today())
        host = st.selectbox("기주 수목(나무 종류)", ["소나무", "느티나무", "벚나무", "참나무", "기타"])
        pest = st.text_input("병해충 이름 (모를 경우 특징 기재)")
        location = st.text_input("상세 위치")
        photo = st.file_uploader("현장 사진 업로드", type=['jpg', 'png', 'jpeg'])
        
        submitted = st.form_submit_button("제보하기")
        if submitted:
            st.success(f"{host}에 발생한 {pest} 제보가 접수되었습니다!")

with col2:
    st.header("🗺️ 실시간 발생 현황")
    # 샘플 데이터 (나중에 실제 데이터로 바꿀 거예요)
    sample_data = pd.DataFrame({
        'lat': [37.01, 37.02, 37.015],
        'lon': [128.82, 128.83, 128.825]
    })
    st.map(sample_data)
