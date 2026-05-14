from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()
# import os
st.header("Hugging Face ChatBOT")

token = "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"

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct:sambanova",
    task="text-generation",
    huggingfacehub_api_token=token
)
model = ChatHuggingFace(llm=llm)
input_text= st.text_input("Enter Your Question here")
if st.button("Ask Question"):
    result = model.invoke(input_text)
    st.write(result.content)