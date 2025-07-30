from fastapi import FastAPI , HTTPException
from dotenv import load_dotenv
from pymongo import MongoClient
from explore_audio import play_audio
import os

app=FastAPI()

@app.get("/")
def root():
    return {'message from sayit':"backend running"}

play_audio()