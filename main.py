from fastapi import FastAPI

app = FastAPI()
#http://127.0.0.1:8000/ para acessar no navegador
@app.get("/helloword")
async def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/teste1 para acessar no navegador
@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo!"}