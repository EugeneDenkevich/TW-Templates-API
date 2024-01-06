from typing import Final

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.application.app import App
from api.apps.auth.routers import routers as auth_routers
from api.settings import settings

app: Final[FastAPI] = App(title="Templates App")

app.add_routers(
    auth_routers,
)

allow_origins = settings.CORS_ALLOW_ORIGINS.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
