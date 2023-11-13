import pytest
from lib.present import *

"""
Test wrapping a present then unwrapping it
"""
def test_wrap():
    present = Present()
    present.wrap('banana')
    assert present.unwrap() == 'banana'

"""
Test wrapping when a present is already wrapped
"""
def test_already_wrapped():
    present = Present()
    present.wrap('banana')
    with pytest.raises(Exception) as e:
        present.wrap('apple')
    error_msg = str(e.value)
    assert error_msg == 'A contents has already been wrapped.'


"""
Test unwrapping a present when a present hasn't been wrapped
"""
def test_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_msg = str(e.value)
    assert error_msg == 'No contents have been wrapped.'


