from lib.greet import *

def test_says_hello_dave():
    result = greet('Dave')
    assert result == 'Hello, Dave!'