
from fastapi import FastAPI

from backend.app.api.users import router as users_router

app = FastAPI(
    title="DevTrack API",
    description="Student and Career Management Platform",
    version="1.0.0"
)

app.include_router(users_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to DevTrack!",
        "status": "API is running"
    }
