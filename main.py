import streamlit as st

st.title('나의 첫 웹 서비스 만들기!!')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 : ')
mbti = st.selectbox('MBTI를 선택해주세요:', ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP'])

# MBTI 설명 데이터 (예시, 실제 데이터는 더 구체적일 수 있음)
mbti_data = {
    'INTJ': {
        '특징': '전략적 사고, 높은 독립성, 계획적',
        '직업': '과학자, 엔지니어, 교수',
        '잘 맞는 MBTI': ['ENFP', 'ENTP']
    },
    'INFP': {
        '특징': '이상주의적, 감정적, 예술적',
        '직업': '작가, 예술가, 상담사',
        '잘 맞는 MBTI': ['ENFJ', 'ESFJ']
    },
    # 다른 MBTI 유형들도 추가 가능
}

if st.button('특징 생성'):
    if mbti in mbti_data:
        특징 = mbti_data[mbti]['특징']
        직업 = mbti_data[mbti]['직업']
        잘_맞는_mbti = ', '.join(mbti_data[mbti]['잘 맞는 MBTI'])

        st.write(f"{name}님! 당신의 MBTI 유형은 {mbti}입니다!")
        st.write(f"**특징**: {특징}")
        st.write(f"**어울리는 직업**: {직업}")
        st.write(f"**잘 맞는 MBTI 유형**: {잘_맞는_mbti}")
    else:
        st.write(f"{name}님! 아직 {mbti} 유형에 대한 정보가 없습니다.")
