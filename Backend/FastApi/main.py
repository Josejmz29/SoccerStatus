from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def root():
    return "¡Hola FastApi!"

@app.get("/url")
async def url():
    return  { "url:": "http://127.0.0.1:8000" }

#documentacion con swagger: http://127.0.0.1:8000/docs
# main:app --reload