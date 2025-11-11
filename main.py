from fastapi import FastAPI

from routes import api_router

app = FastAPI(title="WorkoutAPI")
app.include_router(api_router)
