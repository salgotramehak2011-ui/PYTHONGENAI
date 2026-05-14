# from langchain_core.prompts import ChatPromptTemplate 
# import streamlit as st 
# import uvicorn
# from langchain_core.output_parsers import StrOutputParser 
# from dotenv import load_dotenv # to load environment variables 
# from langchain_ollama import OllamaLLM
# from fastapi import FastAPI
# from langserve import add_routes
# import os 
# load_dotenv()
# #pip install sse_starlettev
# app = FastAPI(title="LangServer API")
# prompt= ChatPromptTemplate.from_template(
#     "Write a creative song about {song} in   100 words"
# )
# llm=OllamaLLM(model="gemma3:1b")

# add_routes(
#     app,
#     prompt|llm,
#     path='/song'   
# )

# if __name__=="__main__":
#     uvicorn.run(app,host='localhost',port=8000)