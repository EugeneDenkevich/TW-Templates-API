from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi.exceptions import HTTPException
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from api.apps.auth.auth import get_auth_router
from api.apps.auth.base_config import current_user
from api.apps.auth.base_config import fastapi_users
from api.apps.auth.manager import password_helper
from api.apps.auth.models import User
from api.apps.auth.schemas import ChangePassword
from api.apps.auth.schemas import UserCreate
from api.apps.auth.schemas import UserRead
from api.database import get_async_session
from api.settings import settings

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
me_router = APIRouter(prefix="/users", tags=["Users"])


auth_router.include_router(get_auth_router())


@me_router.get("/me", response_model=UserRead)
async def get_me(user: User = Depends(current_user)):
    return user


# -------------------


responses_400 = {
    "description": "",
    "content": {
        "application/json": {
            "examples": {
                "Wrong password": {
                    "value": {
                        "detail": "Current password is wrong",
                    },
                },
                "New match old": {
                    "value": {
                        "detail": "New password fully match current password",
                    },
                },
                "New doesn't match new": {
                    "value": {
                        "detail": "New password doesn't match",
                    },
                },
            }
        }
    },
}

responses_200 = {
    "description": "",
    "content": {
        "application/json": {
            "examples": {
                "Success": {
                    "value": {
                        "status": "Password changed successfuly.",
                    },
                },
            }
        }
    },
}


@me_router.post(
    "/change_password", responses={200: responses_200, 400: responses_400}
)
async def change_password(
    passwords: ChangePassword,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    current_password = passwords.current_password
    new_password = passwords.new_password
    new_password_confirm = passwords.new_password_confirm
    verified, _ = password_helper.verify_and_update(
        current_password, user.hashed_password
    )

    # Validate password
    if not verified:
        raise HTTPException(
            detail="Current password is wrong", status_code=400
        )
    if new_password == current_password:
        raise HTTPException(
            detail="New password fully match current password", status_code=400
        )
    if new_password != new_password_confirm:
        raise HTTPException(
            detail="New password doesn't match", status_code=400
        )

    # Save new password
    new_hashed_password = password_helper.hash(new_password)
    stmt = (
        update(User)
        .where(User.email == user.email)
        .values(hashed_password=new_hashed_password)
    )
    await session.execute(stmt)
    await session.commit()

    # Give response
    return {"status": "Password changed successfuly."}


if settings.DEBUG is True:
    auth_router.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate)
    )


routers = (
    auth_router,
    me_router,
)


__all__ = ("routers",)
