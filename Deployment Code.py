# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:41:46 2024

@author: Irfan
"""

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained SVM model
model = joblib.load('svm_model.pkl')

# Title of the web app
st.title("SVM Model Deployment: Should the Customer Receive a Bonus?")

# Input for Customer Name
customer_name = st.text_input("Customer Name")

# Input fields for the features with actual feature names
st.header("Enter the Customer Features:")

# Inputs corresponding to feature names
age = st.number_input("Age", min_value=0)
gender = st.selectbox("Gender", options=[0, 1])  # Assuming 0 = Female, 1 = Male
income_level = st.number_input("Income Level", min_value=0)
winning_percentage = st.number_input("Winning Percentage", min_value=0.0, max_value=100.0)
days_since_last_bet = st.number_input("Days Since Last Bet", min_value=0)
active_days = st.number_input("Active Days", min_value=0)
total_bet_amount = st.number_input("Total Bet Amount", min_value=0.0)
total_won_amount = st.number_input("Total Won Amount", min_value=0.0)
average_bet_amount = st.number_input("Average Bet Amount", min_value=0.0)
bonus_history = st.number_input("Bonus History", min_value=0)
last_bet_amount = st.number_input("Last Bet Amount", min_value=0.0)
total_bets_placed = st.number_input("Total Bets Placed", min_value=0)
total_bets_won = st.number_input("Total Bets Won", min_value=0)
total_days_active = st.number_input("Total Days Active", min_value=0)

def predict_bonus_allocation(features):
    # If you're working with a DataFrame and dropping columns
    # you can use a DataFrame to encapsulate the input features
    data = pd.DataFrame(features, columns=[
        'Age', 'Gender', 'Income Level', 'Winning Percentage',
        'Days Since Last Bet', 'Active Days', 'Total Bet Amount',
        'Total Won Amount', 'Average Bet Amount', 'Bonus History',
        'Last Bet Amount', 'Total Bets Placed', 'Total Bets Won', 'Total Days Active'
    ])
    
    # Ensure 'Customer ID' and 'Customer Name' exist before dropping them
    if 'Customer ID' in data.columns and 'Customer Name' in data.columns:
        data = data.drop(['Customer ID', 'Customer Name'], axis=1)
    else:
        st.warning("Customer ID and Customer Name columns are not found in the dataset.")

    # Return prediction
    return model.predict(data)

# Button to make predictions
if st.button("Predict"):
    # Prepare the feature array
    features = np.array([[age, gender, income_level, winning_percentage, days_since_last_bet,
                          active_days, total_bet_amount, total_won_amount, average_bet_amount,
                          bonus_history, last_bet_amount, total_bets_placed, total_bets_won,
                          total_days_active]])

    # Make prediction
    try:
        prediction = predict_bonus_allocation(features)
        result = "Yes" if prediction[0] == 1 else "No"
        st.success(f"Customer {customer_name} should receive a bonus: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
