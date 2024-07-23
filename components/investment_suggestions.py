# components/investment_suggestions.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = KEY)

def investment_suggestions():
    st.header("Investment Suggestions")
    user_input = st.text_area("Enter your financial data and goals:")
    if st.button("Get Suggestions"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":"Investment Suggestor",
                "content":f"You are a investment suggesor"
            },
            {
                "role":"User",
                "content":f"Provide investment suggestions based on the following data:\n{user_input}"

            }],
            max_tokens=1000
        )
        st.write(response.choices[0].message.content.strip())
