# components/financial_health.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = KEY)

def financial_health():
    st.header("Financial Health Analysis")
    user_input = st.text_area("Enter your financial data for analysis:")
    if st.button("Analyze"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "system",
                "content":f"You are a financial health analyzer"
            },
            {
                "role":"user",
                "content":f"Analyze the following financial data and provide health tips:\n{user_input}"
            }],
            max_tokens=1000
        )
        st.write(response.choices[0].message.content.strip())
