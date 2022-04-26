from fastapi import FastAPI
from routes.Bot_Questions import QuestionsRouter
from routes.Bot_Responses import ResponsesRouter
from routes.movieAPI import movie
from routes.musicApi import music

app = FastAPI()
app.include_router(movie) 
app.include_router(music)
app.include_router(QuestionsRouter) 
app.include_router(ResponsesRouter)