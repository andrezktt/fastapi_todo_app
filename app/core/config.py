from typing import List
from decouple import config
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = 'TODOFast'
    API_V1_STR = '/api/v1'
    
    JWT_SECRET_KEY = config('JWT_SECRET_KEY', cast=str)
    JWT_REFRES_SECRET_KEY = config('JWT_REFRESH_SECRET_KEY', cast=str)
    
    ALGORITHM = 'HS256'
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # Database Connection
    MONGO_CONNECTION_STRING = config('MONGO_CONNECTION_STRING', cast=str)
    
    class Config:
        case_sensitive = True
        
settings = Settings()