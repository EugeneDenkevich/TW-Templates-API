from typing import final

from apps.auth.manager import get_user_manager
from apps.auth.models import User
from fastapi_users import FastAPIUsers
from fastapi_users import models
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.jwt import generate_jwt
from settings import settings

cookie_transport = CookieTransport(
    cookie_name="ownertkn", cookie_max_age=settings.TIME_TOKEN_EXPIRED
)


@final
class TemplateJWTStrategy(JWTStrategy):
    async def write_token(self, user: models.UP) -> str:
        user_status = user.is_superuser
        data = {
            "sub": str(user.id),
            "is_superuser": user_status,
            "aud": self.token_audience,
        }
        return generate_jwt(
            data,
            self.encode_key,
            self.lifetime_seconds,
            algorithm=self.algorithm,
        )


@final
def get_jwt_strategy() -> TemplateJWTStrategy:
    return TemplateJWTStrategy(
        secret=settings.SECRET_AUTH, lifetime_seconds=3600
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
