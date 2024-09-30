import streamlit as st
import pandas as pd
import requests

st.header("Uefa Champions League Trivia!!!")

messsage = st.chat_input("Welcome! Ask me anything about UCL")
print(messsage)

if "messages" not in st.session_state:
    st.session_state.messages = []

if messsage:
    st.session_state.messages.append(('human', messsage))
    for past_msg in st.session_state.messages:
        with st.chat_message(past_msg[0]):
            response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"text/plain"})
            st.markdown(response.text)

    
    with st.chat_message("ai"):
        st.markdown("AC MILAN is the best")