from langchain_core.prompts import ChatPromptTemplate 
import streamlit as st 
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv # to load environment variables 
from langchain_ollama import OllamaLLM
import os 
load_dotenv()
# os.environ['LANGSMITH_API_KEY']=os.getenv('LANGSMITH_API_KEY')
# os.environ['LANGSMITH_TRACING']=os.getenv('LANGSMITH_TRACING')
prompt= ChatPromptTemplate.from_template(
    "Write a creative song about {song} in 100 words"
)
st.title("SongBOT")
llm=OllamaLLM(model="gemma3:1b")
input_text= st.text_input("Enter Song title...")
output= StrOutputParser()   

chain= prompt|llm|output

if input_text:
    st.write(chain.invoke({"song":input_text}))