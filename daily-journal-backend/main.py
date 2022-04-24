from fastapi import FastAPI
from routes.generateSomethingToSay import generate
app = FastAPI()

app.include_router(generate) 