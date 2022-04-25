from fastapi import FastAPI
from routes.Bot_Questions import QuestionsRouter
from routes.Bot_Responses import ResponsesRouter

app = FastAPI()

app.include_router(QuestionsRouter) 
app.include_router(ResponsesRouter)