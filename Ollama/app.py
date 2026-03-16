import os
from dotenv import load_dotenv

load_dotenv()


#langsmithTracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#ChatPromptTemplate->Simple Single prompt template
#from_messages->chat style prompts (system+user)

prompt=ChatPromptTemplate.from_messages(

    [
        ("system","You are helpful assistant.Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#Streamlit framework

st.title("Demo With Google Gemma")
input_Text=st.text_input("What Question you have in your mind?")

llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_Text:
    st.write(chain.invoke({"question":input_Text}))
