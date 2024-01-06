from typing import Annotated

from fastapi.param_functions import Form


class UserOAuth2PasswordRequestForm:
    def __init__(
        self,
        *,
        email: Annotated[
            str,
            Form(),
        ],
        password: Annotated[
            str,
            Form(),
        ],
    ):
        self.username = email
        self.password = password
