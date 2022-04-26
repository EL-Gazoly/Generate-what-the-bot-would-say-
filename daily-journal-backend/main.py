from fastapi import FastAPI
from routes.Bot_Questions import QuestionsRouter
from routes.Bot_Responses import ResponsesRouter
from routes.Bot_Recommendations import RecommendationsRouter

app = FastAPI()
app.include_router(RecommendationsRouter) 
app.include_router(QuestionsRouter) 
app.include_router(ResponsesRouter)