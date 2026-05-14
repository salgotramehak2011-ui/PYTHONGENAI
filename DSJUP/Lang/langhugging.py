from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()
# import os
st.header("Hugging Face ChatBOT")


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct:sambanova",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)
input_text= st.text_input("Enter Your Question here")
if st.button("Ask Question"):
    result = model.invoke(input_text)
    st.write(result.content)