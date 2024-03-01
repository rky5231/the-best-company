import streamlit as st
import pandas

from send_email import send_email

st.title("Contact Us")
df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox(
        'What topic do you want to discuss?',
        df['topic']
    )
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email for {option}

From: {user_email}
{raw_message}
"""
    submitted = st.form_submit_button("Submit")
    if submitted:
        send_email(message)
        st.info("Your message was sent successfully.")

        