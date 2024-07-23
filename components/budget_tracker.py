import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def budget_tracker():
    st.header("Budget Tracker")
    
    # Collect user inputs
    st.subheader("Enter Your Monthly Income and Expenses")
    
    # User inputs for income and expenses
    monthly_income = st.number_input("Monthly Income ($)", min_value=0.0, format="%.2f")
    rent = st.number_input("Rent/Mortgage ($)", min_value=0.0, format="%.2f")
    groceries = st.number_input("Groceries ($)", min_value=0.0, format="%.2f")
    utilities = st.number_input("Utilities ($)", min_value=0.0, format="%.2f")
    entertainment = st.number_input("Entertainment ($)", min_value=0.0, format="%.2f")
    others = st.number_input("Others ($)", min_value=0.0, format="%.2f")
    
    # Create a DataFrame with user inputs
    data = {
        'Category': ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Others'],
        'Amount': [rent, groceries, utilities, entertainment, others]
    }
    df = pd.DataFrame(data)
    
    # Display the data and plot
    st.subheader("Your Budget Overview")
    st.write(df)
    
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Category', y='Amount', ax=ax, color='skyblue')
    plt.title('Monthly Expense Breakdown')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    st.pyplot(fig)

# Call the function to run the Streamlit app
if __name__ == "__main__":
    budget_tracker()
