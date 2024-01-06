from typing import final

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy

from api.apps.auth.manager import get_user_manager
from api.apps.auth.models import User
from api.settings import settings

cookie_transport = CookieTransport(
    cookie_name="ownertkn", cookie_max_age=settings.TIME_COOKIE_EXPIRED
)


@final
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRET_AUTH,
        lifetime_seconds=settings.TIME_TOKEN_EXPIRED,
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
