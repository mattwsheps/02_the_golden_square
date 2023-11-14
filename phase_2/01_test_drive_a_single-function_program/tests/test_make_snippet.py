import pytest
from lib.make_snippet import *

"""
Test output is correct when more than 5
"""
def test_make_snippet():
    input_string = "Hello, my name is Dave and I like cheese"
    assert make_snippet(input_string) == "Hello, my name is Dave..."

"""
Test correct output when string is 1 word
"""
def test_snippet_input_1_word():
    input_string = "Hello"
    assert make_snippet(input_string) == "Hello"

"""
Test correct ouptut when string is < 5
"""
def test_snippet_input_less_than_five_words():
    input_string = "Hello, my name"
    assert make_snippet(input_string) == "Hello, my name"

"""
Test error message is output when input not str
"""
def test_input_type_is_correct():
    input_string = 1
    with pytest.raises(Exception) as e:
        output = make_snippet(input_string)
    error_message = str(e.value)
    assert error_message == "Please input a string"

