import os

from dotenv import load_dotenv

load_dotenv()

APP_DB_URL = os.getenv("APP_DB_URL")
ALEMBIC_DB_URL = os.getenv("ALEMBIC_DB_URL")

SECRET_AUTH = os.getenv("SECRET_AUTH")
