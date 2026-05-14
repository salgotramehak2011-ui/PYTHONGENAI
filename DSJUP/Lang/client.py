# import streamlit as st
# import requests 
# from dotenv import load_dotenv
# load_dotenv()
# def get_ollama(input_text):
#     response=requests.post("http://127.0.0.1:8000/song/invoke",json={'input':{'song':input_text}})
#     return response.json()['outpu']

# st.title("Langserve API")
# input_text= st.text_input("Write a song on ")
# if input_text:
#     st.write(get_ollama(input_text))