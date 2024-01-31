from typing import Final

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.application.app import App
from api.apps.auth.routers import routers as auth_routers
from api.apps.menu.routers import routers as menu_routers
from api.settings import settings

docs_url = None
redoc_url = None

if settings.DEBUG:
    docs_url = "/docs"
    redoc_url = "/redoc"


app: Final[FastAPI] = App(
    title="Templates App",
    debug=settings.DEBUG,
    docs_url=docs_url,
    redoc_url=redoc_url,
)

app.add_routers(
    auth_routers,
    menu_routers,
)

allow_origins = settings.CORS_ALLOW_ORIGINS.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
