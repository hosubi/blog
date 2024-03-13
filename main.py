# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.header('블로그 :red[소제목 서론 생성기!]', divider='rainbow')
st.write('지수 상승과 체류시간 상승!:exclamation:')
       
content = st.text_input('주제, 키워드 입력!  :memo:, !')
prompt = '''blog marketing storyteller!, #keyword, #title = write 3 sentences of the storytelling copywriting introduction, 3 hooking (#Real benefits vs. concern, opportunity cost case by comparison in inconvenience if not) title recommendation, anchor effect citation for persuasion!

Condition: Regarding the #keyword topic,
Quoting celebrities or books, there are no naturally duplicated documents like humans, they are reliable, sentences are easy and readable!

100% 사람과 같이!
Write by referring to 4 conditions (commands, conditions, yes, format) !!
Correct in Korean!!
천천히 답변! 결과값만 보여줘!
#:'''


if st.button('블로그 소제목 서론 생성기!'):
    with st.spinner('시간이 걸릴 수 있어요! 기다려주세요! 추천 중...'):
        result = chat_model.predict( prompt + content )
        st.write(result)

  


st.link_button("토스후원하기, :passenger_ship:", "https://toss.me/aicopy")
st.link_button("buy me a coffee, :coffee:", "https://www.buymeacoffee.com/aicopy")

st.subheader('SNS 추천글!', divider='rainbow') 
st.link_button("광고문의 :coffee:", "https://open.kakao.com/o/s0ic2hMf")
