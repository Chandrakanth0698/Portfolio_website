import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your email",key="input_user_email")
    raw_message = st.text_area("Type message", height=8,key="input_message")
    message = f"""\
Subject: Email from Portfolio App

From:{user_email}
message:{raw_message}
"""
    sub_button = st.form_submit_button()
    if sub_button:
        send_email(message,password=st.secrets["SMTP_GMAIL_PASSWORD"])
        st.info("Email sent successfully")


