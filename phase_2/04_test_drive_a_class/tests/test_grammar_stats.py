from lib.grammar_stats import *

"""
Given a text that doesn't start with a capital letter and doesn't end with a suitable punctuation mark
#check will return False
"""
def test_no_capital_no_punc():
    grammar_stats = GrammarStats()
    text = 'words are words'
    result = grammar_stats.check(text)
    assert result == False

"""
Given a text that starts with a capital letter and ends with a full stop
#check will return True
"""
def test_capital_full_stop():
    text = 'Words are words.'
    grammar_stats = GrammarStats()
    result = grammar_stats.check(text)
    assert result == True

"""
Given a text that starts with a capital letter and ends with a question mark
#check will return True
"""
def test_capital_q_mark():
    text = 'Words are words?'
    grammar_stats = GrammarStats()
    result = grammar_stats.check(text)
    assert result == True

"""
Given a text that starts with a capital letter and ends with an exclamation mark
#check will return True
"""
def test_capital_e_mark():
    text = 'Words are words!'
    grammar_stats = GrammarStats()
    result = grammar_stats.check(text)
    assert result == True

"""
Given a text that doesn't start with a capital letter and ends with a suitable punctuation mark
#check will return False
"""
def test_no_capital_punc():
    text = 'words are words!'
    grammar_stats = GrammarStats()
    result = grammar_stats.check(text)
    assert result == False

"""
Given a text that starts with a capital letter and doesn't end with a suitable punctuation mark
#check will return False
"""
def test_capital_no_punc():
    text = 'Words are words'
    grammar_stats = GrammarStats()
    result = grammar_stats.check(text)
    assert result == False

"""
Given 5 texts, 2 valid and 3 invalid
#percentage_good returns 40
"""
def test_2_valid_3_invalid():
    texts = [
        'Hello my name is.',
        'hello my name is',
        'Hello my name is!',
        'hello my name is',
        'hello my name is',
    ]
    grammar_stats = GrammarStats()
    for text in texts:
        grammar_stats.check(text)
    result = grammar_stats.percentage_good()
    assert result == 40

"""
Given 5 texts, 5 valid
#percentage_good returns 100
"""
def test_all_valid():
    texts = [
        'Hello my name is.',
        'Hello my name is.',
        'Hello my name is?',
        'Hello my name is.',
        'Hello my name is!',
    ]
    grammar_stats = GrammarStats()
    for text in texts:
        grammar_stats.check(text)
    result = grammar_stats.percentage_good()
    assert result == 100

"""
Given 5 texts, 0 valid
#percentage_good returns 0
"""
def test_none_valid():
    texts = [
        'hello my name is,',
        'hello my name is',
        'hello my name is',
        'hello my name is',
        'hello my name is',
    ]
    grammar_stats = GrammarStats()
    for text in texts:
        grammar_stats.check(text)
    result = grammar_stats.percentage_good()
    assert result == 0