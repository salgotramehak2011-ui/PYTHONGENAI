# built-in module - venv 
# python -m venv myproject

#  pip install -r requirements.txt 

from langchain_core.prompts import ChatPromptTemplate 
import streamlit as st 
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv # to load environment variables 
from langchain_ollama import OllamaLLM
prompt= ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant, please respond to user queries."),
        ("user","Question:{question}")
    ]
)
st.title("ChatBOT")
llm=OllamaLLM(model="gemma3:1b")
input_text= st.text_input("Enter Your Question here...")
output= StrOutputParser()


chain= prompt|llm|output

if input_text:
    st.write(chain.invoke({"question":input_text}))

# from ollama import chat

# response = chat(
#     model='gemma3:1b',
#     messages=[{'role': 'user', 'content': 'Hello!'}],
# )
# print(response.message.content)