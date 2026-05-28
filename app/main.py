from fastapi import FastAPI
from pydantic import BaseModel 

app=FastAPI()
class UserQuestion(BaseModel):
    question:str
    
@app.get("/")
def home():
    return{"message": "RAG API is running"}

@app.post("/ask")
def ask_question(heAsked: UserQuestion):
    return{
        "question_asked": heAsked.question
    }