from lib.report_length import *

def test_correct_example_1():
    result = report_length('Hello.')
    assert result == "This string was 6 characters long."

def test_correct_example_2():
    result = report_length('Happiness')
    assert result == "This string was 9 characters long."

