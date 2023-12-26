from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth.base_config import auth_backend
from src.auth.base_config import fastapi_users
from src.auth.schemas import UserCreate
from src.auth.schemas import UserRead


app = FastAPI(title="Travell App")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
