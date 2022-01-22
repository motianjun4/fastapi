from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from utils import ResponseType, response
from NLP.index import analyzer
    
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

@app.get("/")
async def root():
    return response(ResponseType.SUCCESS, "Hello world!")

@app.get("/calc/add/")
async def read_item(a: int = None, b: int = None):
    if a is None or b is None:
        return response(ResponseType.ERROR, None, "Please specify query parameters a:int and b:int")
    return response(ResponseType.SUCCESS, a+b)

@app.get("/nlp/sentiment")
async def sentiment_analysis(text: str = None):
    if text is None:
        return response(ResponseType.ERROR, None, "Please specify query parameter text:str")
    return response(ResponseType.SUCCESS, analyzer.score(text))

uvicorn.run(app, host="0.0.0.0", port=8000)
