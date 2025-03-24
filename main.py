import random

from fastapi import FastAPI

app = FastAPI()
#http://127.0.0.1:8000/ para acessar no navegador
@app.get("/")
async def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/teste1 para acessar no navegador
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(a: 0, b: 1000)}