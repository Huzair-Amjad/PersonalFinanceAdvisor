# main.py
import streamlit as st
from components.budget_tracker import budget_tracker
from components.goal_setting import goal_setting
from components.investment_suggestions import investment_suggestions
from components.financial_health import financial_health

st.title("AI-powered Personal Finance Advisor")

menu = ["Budget Tracker", "Goal Setting", "Investment Suggestions", "Financial Health Analysis"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Budget Tracker":
    budget_tracker()
elif choice == "Goal Setting":
    goal_setting()
elif choice == "Investment Suggestions":
    investment_suggestions()
elif choice == "Financial Health Analysis":
    financial_health()
