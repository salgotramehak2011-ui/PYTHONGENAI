import streamlit as st
import pickle
import pandas as pd
import numpy as np
# import joblib
# Load the trained model
model = pickle.load(open("heart_model.pkl","rb"))
# model = joblib.load("heart_model.pkl")
# create a streamlit app
age = st.number_input("Age", min_value=1, max_value=120, values=30)
sex = st.selectbox("Sex", options=["Male","Female"])
cholestrol = st.number_input("Cholestrol", min_value=1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        `)