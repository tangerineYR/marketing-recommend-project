import streamlit as st

def recommend_marketing(age, job, month, contact, poutcome):
    score = 0
    
    # 직업 (가장 높은 가입률 순)
    if job in ['student', 'retired']:
        score += 3
    elif job in ['unemployed', 'management', 'admin.']:
        score += 2
    elif job in ['self-employed', 'unknown', 'technician']:
        score += 1
    
    # 연령대 (실제 분석 기반)
    if age <= 25 or age >= 50:  # 20대 이하, 50대 이상
        score += 2
    elif 30 <= age < 40:
        score += 1
    
    # 연락 월 (높은 성공률 월)
    if month in ['mar', 'sep', 'oct', 'dec']:
        score += 2
    
    # 연락 방식
    if contact == 'cellular':
        score += 2
    elif contact == 'telephone':
        score += 1
    # unknown은 0점
    
    # 이전 캠페인 결과 (가장 강력한 예측 인자)
    if poutcome == 'success':
        score += 4  # 64.7% 재가입률
    elif poutcome == 'failure':
        score -= 1
    
    # 결과 반환
    if score >= 8:
        return "적극 추천! (가입 가능성 매우 높음)"
    elif score >= 5:
        return "추천 (가입 가능성 높음)"
    elif score >= 3:
        return "보통 (신중히 고려)"
    else:
        return "비추천 (가입 가능성 낮음)"

# Streamlit UI
st.title("정기예금 마케팅 대상 추천")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("나이", min_value=18, max_value=100, value=35)
    job = st.selectbox("직업", [
        "student", "retired", "unemployed", "admin.", "management", 
        "unknown", "self-employed", "technician", "services", 
        "housemaid", "entrepreneur", "blue-collar"
    ])

with col2:
    month = st.selectbox("연락 월", [
        "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec"
    ])
    contact = st.selectbox("연락 방식", ["cellular", "telephone", "unknown"])

poutcome = st.radio("이전 캠페인 결과", ["success", "failure", "unknown"])

if st.button("가입 가능성 분석"):
    result = recommend_marketing(age, job, month, contact, poutcome)
    
    if "적극 추천" in result:
        st.success(result)
    elif "추천" in result:
        st.info(result)
    elif "보통" in result:
        st.warning(result)
    else:
        st.error(result)
