from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

@app.get('/')
async def hello_world():
    return 'Hello, world!'