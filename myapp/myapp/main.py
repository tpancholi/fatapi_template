"""The entry point for the app"""
from fastapi import FastAPI

app = FastAPI(title="RestAPI", description="My FastAPI Template")

@app.get("/")
async def health_check():
    return {"status": "ok"}

