from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os

#langserve deploys application as restapis
from langserve import add_routes #for creating apis
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)


#1.Chat Template

system_template="Translate the following into {language}:"

prompt_template=ChatPromptTemplate(
    [
        ("system",system_template),
        ("user","{text}")
    ]
)

parser=StrOutputParser()

#chain
chain=prompt_template|model|parser


#App definition
app=FastAPI(
    title="langchain Server",
    version="1.0",
    description="A single API server using Langchain runnable interfaces"
)


#Adding chain routes
#add_routes is a function used to connect a langchain or runnable to fastapi endpoint automatically
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn#To run fast apis 
    #vicorn is a server to run python applications like fastapis,Starlette
    uvicorn.run(app,host="localhost",port=8000)