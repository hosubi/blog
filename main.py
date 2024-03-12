# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.header('블로그 :red[소제목 서론 생성기!]', divider='rainbow')
st.write('지수 상승과 체류시간 상승!:exclamation:')
       
content = st.text_input('주제, 키워드 입력!  :memo:, !')
prompt = '''blog marketing storyteller!, #keyword, #deliver the title, write 3 sentences of the storytelling copywriting introduction, 3 hooking (#Real benefits vs. concern, opportunity cost case by comparison in inconvenience if not) title recommendation, anchor effect citation for persuasion!

Condition: Regarding the #keyword topic,
Quoting celebrities or books, there are no naturally duplicated documents like humans, they are reliable, sentences are easy and readable!


Example:
(Introduction: 관절연골 문제는 나이를 불문하고 많은 이들이 공통으로 겪는 불편함 중 하나입니다. 특히, 우리가 사랑하는 가족들이 이러한 문제로 고생하는 것을 보면, 더욱 마음이 아픕니다. 저희 가정에서도 어르신들께서는 항상 "젊을 때부터 몸 관리를 잘해야 한다"고 강조하셨습니다.

[Leveraging character experience: Starting a story through a celebrity or personal experience.
Problem Awareness: presentation of a problem the reader can relate to.
Solution Introduction: Presenting a product or service as a solution.
Emphasis on ingredients and efficacy: Explaining the main ingredients of the product and its efficacy.
Emotional connection: the creation of emotional empathy through personal stories or success stories.
Call to action: Steps to induce the reader to act, such as purchasing or requesting additional information.
Induce continuous interest: providing content that the reader can read through and think about afterwards.]


Write by referring to 4 conditions (commands, conditions, yes, format) !!
Correct in Korean!!
#:'''


if st.button('블로그 소제목 서론 생성기!'):
    with st.spinner('시간이 걸릴 수 있어요! 기다려주세요! 추천 중...'):
        result = chat_model.predict( prompt + content )
        st.write(result)

  


st.link_button("토스후원하기, :passenger_ship:", "https://toss.me/aicopy")
st.link_button("buy me a coffee, :coffee:", "https://www.buymeacoffee.com/aicopy")

st.subheader('SNS 추천글!', divider='rainbow') 
st.link_button("광고문의 :coffee:", "https://open.kakao.com/o/s0ic2hMf")
