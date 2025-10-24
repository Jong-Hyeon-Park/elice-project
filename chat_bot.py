import streamlit as st
from dotenv import load_dotenv
from llm import get_assistant_message



st.set_page_config(page_title="알레르기 정보", page_icon="🤧")
st.title("음식 알레르기 정보 챗봇")
st.caption("음식명이나 성분을 입력하면 알레르기 위험 성분을 알려드립니다.")


load_dotenv()

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("성분을 입력하고 알레르기 정보를 확인하세요."):

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("답변을 생성하는 중입니다"):
      assistant_response = get_assistant_message(prompt)
      with st.chat_message("assistant"):
        st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})