from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Smart Monitoring System Running"
    }

@app.get("/latest")
def latest():

    if os.path.exists("data.json"):

        with open("data.json", "r") as f:
            data = json.load(f)

        return data

    return {
        "temperature": 0,
        "humidity": 0,
        "status": "WAITING",
        "result": "No Data"
    }