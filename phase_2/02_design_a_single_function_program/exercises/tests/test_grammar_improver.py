from lib.grammar_improver import *

"""
Given a text that doesn't start with a capital letter and doesn't end with a suitable punctuation mark
It will return False
"""
def test_no_capital_no_punc():
    text = 'words are words'
    result = grammar_improver(text)
    assert result == False

"""
Given a text that starts with a capital letter and ends with a full stop
It will return True
"""
def test_capital_full_stop():
    text = 'Words are words.'
    result = grammar_improver(text)
    assert result == True

"""
Given a text that starts with a capital letter and ends with a question mark
It will return True
"""
def test_capital_q_mark():
    text = 'Words are words?'
    result = grammar_improver(text)
    assert result == True

"""
Given a text that starts with a capital letter and ends with an exclamation mark
It will return True
"""
def test_capital_e_mark():
    text = 'Words are words!'
    result = grammar_improver(text)
    assert result == True

"""
Given a text that doesn't start with a capital letter and ends with a suitable punctuation mark
It will return False
"""
def test_no_capital_punc():
    text = 'words are words!'
    result = grammar_improver(text)
    assert result == False

"""
Given a text that starts with a capital letter and doesn't end with a suitable punctuation mark
It will return False
"""
def test_capital_no_punc():
    text = 'Words are words'
    result = grammar_improver(text)
    assert result == False