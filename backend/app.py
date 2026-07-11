from fastapi import FastAPI
from backend.routes import router

app = FastAPI(
    title="Personalized Networking Assistant",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend is running successfully!"}