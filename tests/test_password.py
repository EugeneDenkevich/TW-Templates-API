
from testlib.utils import change_password, login


def test_change_password(owner):
    """Check if the password is changing properly."""
    email = owner["email"]
    old_password = owner["password"]
    new_password = "newPassword0987654321"
    
    response = login(email, old_password)
    assert response.status_code == 204
    
    
    cookies = {"ownertkn": response.cookies["ownertkn"]}
    response = change_password(email, old_password, new_password, cookies)
    assert response.status_code == 200
    
    
    response = login(email, new_password)
    assert response.status_code == 204
    
    response = login(email, old_password)
    assert response.status_code == 400

"""
Всё работает. Но нужно поправить структуру тестов. Иначе дальше будет ппц.
"""