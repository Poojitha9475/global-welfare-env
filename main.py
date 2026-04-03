from fastapi import FastAPI
from inference import run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Global Welfare Env Running"}

@app.get("/run")
def run_env():
    run()
    return {"status": "executed"}
