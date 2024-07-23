# components/goal_setting.py
import streamlit as st

def goal_setting():
    st.header("Goal Setting")
    goal = st.text_input("Enter your financial goal:")
    st.write(f"Your goal: {goal}")
