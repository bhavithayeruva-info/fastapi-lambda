from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI working with existing Lambda"}

handler = Mangum(app)
