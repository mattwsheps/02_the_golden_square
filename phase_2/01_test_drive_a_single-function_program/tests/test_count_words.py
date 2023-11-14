import pytest
from lib.count_words import *

"""
Test that a 5 word string will return 5
"""
def test_5_word_string():
    assert count_words('Hello my name is Dave') == 5

"""
Test that a 1 word string will return 1
"""
def test_1_word_string():
    assert count_words('Hello') == 1

"""
Test that an empty string returns 0
"""
def test_empty_string():
    assert count_words('') == 0

"""
Test an error message is outputted when the input is not string
"""
def test_input_not_a_string():
    with pytest.raises(Exception) as e:
        output = count_words(5)
    error_msg = str(e.value)
    assert error_msg == 'The input you provide must be a string.'
    
    