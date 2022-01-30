from fastapi import FastAPI
from platform_api.api.v1 import create_api_router

app = FastAPI()
api_router = create_api_router()

app.include_router(api_router)