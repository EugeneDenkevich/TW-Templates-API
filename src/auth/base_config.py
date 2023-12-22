from fastapi_users import FastAPIUsers
from fastapi_users import models
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.jwt import generate_jwt

from src.auth.manager import get_user_manager
from src.auth.models import User
from src.config import SECRET_AUTH
from src.config import TIME_TOKEN_EXPIRED

cookie_transport = CookieTransport(
    cookie_name="ownertkn", cookie_max_age=TIME_TOKEN_EXPIRED
)


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


def get_jwt_strategy() -> TemplateJWTStrategy:
    return TemplateJWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)


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
