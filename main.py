from fastapi import FastAPI 
import uvicorn
    
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

uvicorn.run(app, host="0.0.0.0", port=8000)
