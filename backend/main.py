from fastapi import FastAPI , HTTPException
from dotenv import load_dotenv
from pymongo import MongoClient
import os

app=FastAPI()

@app.get("/")
def root():
    return {'message from sayit':"backend running"}