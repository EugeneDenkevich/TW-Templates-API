from typing import Final

from apps.auth.base_config import auth_backend
from apps.auth.base_config import fastapi_users
from apps.auth.routers import me_router
from apps.auth.schemas import UserCreate
from apps.auth.schemas import UserRead
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app: Final[FastAPI] = FastAPI(title="Travell App")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(me_router)


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
