from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def root():
    return "¡Hola FastApi!"

@app.get("/url")
async def url():
    return  { "url:": "https://github.com/Josejmz29/SoccerStatus/tree/Backend" }