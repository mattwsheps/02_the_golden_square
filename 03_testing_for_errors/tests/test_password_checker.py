import pytest
from lib.password_checker import *

def test_valid_password():
    password_checker = PasswordChecker()
    assert password_checker.check('1234567890')

def test_invalid_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('hello')
    error_msg = str(e.value)
    assert error_msg == "Invalid password, must be 8+ characters."

