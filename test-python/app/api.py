from fastapi import FastAPI

app = FastAPI()

@app.get('/') # methodとendpointの指定
async def hello():
    return {"text": "hello world!"}

@app.get('/json') # methodとendpointの指定
async def hello():
    return {"text": "Json!"}

@app.get('/api') # methodとendpointの指定
async def hello():
    return {"text": "APIAPIAPI!"}