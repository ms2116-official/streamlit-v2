import streamlit as st

st.set_page_config(
    page_title="스마트 홈 대시보드 - 윤택한",
    layout="wide"
)

st.header("스트림릿 배포 테스트중")
st.write("스트림릿 배포 해보기 - 윤택한")

st.write("스트림릿 배포 내용 추가합니다")

# 페이지 등록
# st.Page("파일경로", title='메뉴이름", icon="아이콘")
# 1. 홈 화면
home = st.Page("pages/home.py", title="홈")
# 2. 센서 화면
sensors = st.Page("pages/sensors.py", title="센서 현황")
# 3. 전력 화면
power  = st.Page("pages/power.py", title="전력현황")

# 네이게이션 구성
pg = st.navigation({
    "메인" : [home],
    "분석" : [sensors, power]
})

st.sidebar.write("같이 사이드바 형태입니다")

# 선택된 페이지 실행
pg.run()