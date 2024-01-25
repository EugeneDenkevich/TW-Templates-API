import httpx

from tests.conftest import BASE_URL


def change_password(email, password, new_password, cookies):
    """
    Change owner password
    """
    response = httpx.post(
        url=f"{BASE_URL}/users/change_password",
        json={
            "current_password": password,
            "new_password": new_password,
            "new_password_confirm": new_password,
        },
        cookies=cookies,
    )

    return response


def login(email, password):
    """
    Login owner
    """

    response = httpx.post(
        url=f"{BASE_URL}/auth/login",
        data={"email": email, "password": password},
    )

    return response
