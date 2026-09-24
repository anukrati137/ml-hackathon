import streamlit as st
st.title("Hello, Hackathon!")
name = st.text_input("Your name")
if name:
    st.sucess(f"Welcome, {name}!")
