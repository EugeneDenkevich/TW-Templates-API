from fastapi import Depends
from fastapi import FastAPI
from uvicorn import run

from src.auth.base_config import auth_backend
from src.auth.base_config import current_user
from src.auth.base_config import fastapi_users
from src.auth.models import User
from src.auth.schemas import UserCreate
from src.auth.schemas import UserRead

app = FastAPI(title="Travell App")

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


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


if __name__ == "__main__":
    run("main:app", reload=True)
