from lib.diary_entry import *

"""
DiaryEntry is constructed with a title and contents
"""
def test_diary_entry_construction():
    entry = DiaryEntry('Monday', 'I walked the dog.')
    assert entry.title == 'Monday' 
    assert entry.contents == 'I walked the dog.'

"""
Given an empty string
#count_words returns 0
"""
def test_count_empty_string():
    entry = DiaryEntry('Monday', '')
    assert entry.count_words() == 0

"""
Given a title and entry of 5 words
#count_words returns 5
"""
def test_count_5_words():
    entry = DiaryEntry('Monday', 'I went to the park.')
    assert entry.count_words() == 5

"""
Given a title and entry of 10 words
#count_words returns 10
"""
def test_count_10_words():
    entry = DiaryEntry('Monday', 'I went to the park. I went to the cinema.')
    assert entry.count_words() == 10
