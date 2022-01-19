from fastapi import FastAPI 
import uvicorn
    
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/calc/add/")
async def read_item(a: int = None, b: int = None):
    if a is None or b is None:
        return {"message": "Please specify query parameters a:int and b:int"}
    return a+b

uvicorn.run(app, host="0.0.0.0", port=8000)
