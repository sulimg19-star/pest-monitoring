import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 앱 설정 및 제목
st.set_page_config(page_title="백두대간 전자야장", layout="wide")

st.title("🌲 수목 병해충 모니터링 전자야장")
st.markdown("현장에서 입력한 데이터를 즉시 엑셀(CSV)로 저장하고 보고서에 활용하세요.")

# 데이터 저장용 주머니
if 'data_list' not in st.session_state:
    st.session_state.data_list = []

col1, col2 = st.columns([1, 2])

with col1:
    st.header("📍 데이터 입력")
    with st.form("field_form", clear_on_submit=True):
        date = st.date_input("조사 날짜", datetime.now())
        host = st.selectbox("기주 수목", ["소나무", "느티나무", "벚나무", "참나무", "기타"])
        pest = st.text_input("병해충명/피해종류 (예: 솔껍질깍지벌레)")
        location = st.text_input("상세 위치 (예: 전시원 A-1 구역)")
        
        submitted = st.form_submit_button("야장 기록 추가")
        if submitted:
            new_entry = {
                "날짜": date.strftime("%Y-%m-%d"),
                "기주수목": host,
                "병해충명": pest,
                "상세위치": location
            }
            st.session_state.data_list.append(new_entry)
            st.success("데이터가 야장에 추가되었습니다!")

with col2:
    st.header("📋 기록된 데이터 목록")
    if st.session_state.data_list:
        df = pd.DataFrame(st.session_state.data_list)
        st.dataframe(df, use_container_width=True)
        
        # 엑셀(CSV) 파일 추출 기능
        csv_data = df.to_csv(index=False).encode('utf-8-sig')
        
        st.markdown("---")
        st.subheader("💾 보고서용 파일 추출")
        st.download_button(
            label="📊 현재 기록 엑셀(CSV) 파일로 저장하기",
            data=csv_data,
            file_name=f"병해충_모니터링_보고서_{datetime.now().strftime('%Y%m%d')}.csv",
            mime='text/csv',
        )
        
        if st.button("🗑️ 야장 초기화"):
            st.session_state.data_list = []
            st.rerun()
    else:
        st.info("아직 입력된 데이터가 없습니다. 왼쪽에서 입력을 시작해 주세요.")
