from cgitb import html
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn

from utils import ResponseType, response
from NLP.index import analyzer
    
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

@app.get("/api/calc/add/")
async def read_item(a: int = None, b: int = None):
    if a is None or b is None:
        return response(ResponseType.ERROR, None, "Please specify query parameters a:int and b:int")
    return response(ResponseType.SUCCESS, a+b)

@app.get("/api/nlp/sentiment")
async def sentiment_analysis(text: str = None):
    if text is None:
        return response(ResponseType.ERROR, None, "Please specify query parameter text:str")
    return response(ResponseType.SUCCESS, analyzer.score(text))

@app.get("/loaderio-d5b4e8ab5d935530190ffd78ffc52665/")
async def loader_verify():
    return "loaderio-d5b4e8ab5d935530190ffd78ffc52665"

app.mount("/", StaticFiles(directory="static", html=True), name="static")
uvicorn.run(app, host="0.0.0.0", port=8000)
