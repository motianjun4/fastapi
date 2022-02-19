from fastapi import FastAPI, Form, UploadFile, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn
import time

from utils.response import ResponseType, response
from NLP.index import analyzer
import CV.label_detection

from utils.logs import logs

CV.label_detection.init()
    
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

@app.middleware("http")
async def request_log(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response: Response
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logs.info({
        "url": str(request.url),
        "status_code": response.status_code,
        "process_time": str(process_time*1000)+"ms",
        "client_ip": request.client.host
    })
    
    return response

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

@app.post("/api/cv/label_detection")
async def label_detection(image:UploadFile = Form(...)):
    if image is None:
        return response(ResponseType.ERROR, None, "Please specify form data 'image'")
    if not CV.label_detection.detector:
        return response(ResponseType.ERROR, None, "not init")
    content = image.file.read()
    
    labels = CV.label_detection.detector.get_labels(content)
    return response(ResponseType.SUCCESS, labels)

@app.get("/loaderio-d5b4e8ab5d935530190ffd78ffc52665/")
async def loader_verify():
    return "loaderio-d5b4e8ab5d935530190ffd78ffc52665"

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
uvicorn.run(app, host="0.0.0.0", port=8000)
