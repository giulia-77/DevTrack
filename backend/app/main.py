from fastapi import FastAPI

app = FastAPI(
    title="DevTrack API",
    description="Student and Career Management Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DevTrack!",
        "status": "API is running"
    }