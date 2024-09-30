import streamlit as st
import pandas as pd

df = pd.read_csv("clwin.csv", index_col=0)

st.title("Champions League Winners!!!")

st.write("All the winners since the beginning of the competition")

st.dataframe(df)

df2 = pd.read_excel("team.xlsx", index_col=0)
st.dataframe(df2)

st.image("testimage.png")

user_input = st.text_input("Ask me a question?")
if user_input:
    st.write("Yes!!")
## python -m streamlit script.py