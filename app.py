import streamlit as st
import pandas as pd
from datetime import datetime

# 앱 설정
st.set_page_config(page_title="백두대간 전자야장", layout="wide")

st.title("🌲 2026 병해충 모니터링 전자야장")
st.write("현장에서 데이터를 입력하고, 하단에서 **엑셀(CSV)** 파일로 추출하세요.")

# 데이터 저장용 세션 상태 초기화
if 'data_list' not in st.session_state:
    st.session_state.data_list = []

col1, col2 = st.columns([1, 2])

with col1:
    st.header("📍 데이터 입력")
    with st.form("monitoring_form", clear_on_submit=True):
        # 1. 발생연도 (2026년 고정)
        st.info("📅 발생연도: 2026년")
        
        # 2. 발생일자 (오늘 날짜 자동 선택)
        occurrence_date = st.date_input("발생일자", datetime.now())
        
        # 3. 구분 (병/해충 선택) - 수림님이 요청하신 부분!
        category = st.radio("구분", ["생물(병)", "생물(해충)"], horizontal=True)
        
        # 4. 서술형 항목들
        exhibition_garden = st.text_input("전시원 (직접 작성)")
        writer = st.text_input("작성자 (직접 작성)")
        plant_name = st.text_input("식물명 (직접 작성)")
        planting_number = st.text_input("식재번호 (직접 작성)")
        cause = st.text_area("피해원인 (서술형 직접 작성)")
        
        # 5. 기타 (기본값 '없음', 필요시 수정)
        etc = st.text_input("기타", value="없음")
        
        submitted = st.form_submit_button("야장 기록 추가")
        
        if submitted:
            # 순번 자동 계산 (리스트 길이에 따라 1번부터 차례대로)
            next_no = len(st.session_state.data_list) + 1
            
            new_entry = {
                "순번": next_no,
                "발생연도": "2026년",
                "발생일자": occurrence_date.strftime("%Y-%m-%d"),
                "구분": category,
                "전시원": exhibition_garden,
                "작성자": writer,
                "식물명": plant_name,
                "식재번호": planting_number,
                "피해원인": cause,
                "기타": etc
            }
            st.session_state.data_list.append(new_entry)
            st.success(f"✅ {next_no}번 데이터가 추가되었습니다!")

with col2:
    st.header("📋 모니터링 기록 목록")
    if st.session_state.data_list:
        df = pd.DataFrame(st.session_state.data_list)
        # 표 보여주기 (인덱스 제외)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # 엑셀(CSV) 추출 버튼
        csv_data = df.to_csv(index=False).encode('utf-8-sig')
        
        st.markdown("---")
        st.subheader("💾 데이터 저장")
        st.download_button(
            label="📊 현재까지 기록 엑셀(CSV) 다운로드",
            data=csv_data,
            file_name=f"병해충_모니터링_결과_{datetime.now().strftime('%Y%m%d')}.csv",
            mime='text/csv',
        )
        
        if st.button("🗑️ 전체 목록 지우기"):
            st.session_state.data_list = []
            st.rerun()
    else:
        st.info("아직 입력된 데이터가 없습니다. 왼쪽에서 입력을 시작해 주세요.")
