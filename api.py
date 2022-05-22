from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import secrets
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
def root():
    try:
        r = requests.get("https://www.reddit.com/r/images/top.json?limit=10&t=month")
        print(r.status_code)
        if r.status_code == 429:
            return HTTPException(status_code=r.status_code, detail=r.json()["message"])
        urls = []
        for i in r.json()["data"]["children"]:
            urls.append(i["data"]["thumbnail"])
        return urls
    except:
        return HTTPException(status_code=500, detail="Internal Server Error")
