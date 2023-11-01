import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Type message", height=8)
    sub_button = st.form_submit_button()
    if sub_button:
        send_email(message)