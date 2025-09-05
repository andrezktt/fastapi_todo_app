from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.user_model import User
from models.todo_model import Todo
from api.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('🔹 Iniciando conexão com o bando de dados...')
    client_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todoapp
    await init_beanie(
        database=client_db,
        document_models=[
            User,
            Todo
        ]
    )
    print('✅ Conexão estabelecida com sucesso.')
    yield
    print('🛑 Encerrando conexão com o banco de dados...')
    client_db.close()

app = FastAPI(
    lifespan=lifespan, 
    title=settings.PROJECT_NAME, 
    openapi_url=f'{settings.API_V1_STR}/openapi.json'
)

app.include_router(
    router=router,
    prefix=settings.API_V1_STR
)