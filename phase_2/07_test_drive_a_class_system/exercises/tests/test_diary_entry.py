from lib.diary_entry import *

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

"""
Given a title and entry of 10 words
and a reading speed of 2 wpm
#reading time returns 5
"""
def test_reading_time_10_words_2_wpm():
    entry = DiaryEntry('Monday', 'I went to the park. I went to the cinema.')
    assert entry.reading_time(2) == 5

