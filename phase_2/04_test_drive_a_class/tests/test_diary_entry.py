from lib.diary_entry import *

"""
Given a title and contents
#format returns a formatted diary entry, like:
"My Title: These are the contents"
"""
def test_format():
    diary_entry = DiaryEntry('My Title', 'These are the contents.')
    assert diary_entry.format() == "My Title: These are the contents."

"""
Given a title and contents
#count_words returns the number of words in the title and contents
"""
def test_count_words():
    diary_entry = DiaryEntry('My Title', 'These are the contents.')
    assert diary_entry.count_words() == 6

"""
Given a wpm of 2 and a contents of 4 words
#reading_time returns 2
"""
def test_reading_time():
    diary_entry = DiaryEntry('My Title', 'These are the contents.')
    assert diary_entry.reading_time(2) == 2

"""
Given a wpm of 2, 1 minutes and a contents of 6 words
#reading_time returns first two words
"""
def test_reading_chunk():
    diary_entry = DiaryEntry('My Title', 'These are the contents this time.')
    assert diary_entry.reading_chunk(2, 1) == 'These are'

"""
Given a wpm of 2, 1 minutes and a contents of 6 words
#reading_time after the second time the function's called it returns 'the contents'
"""
def test_reading_chunk_2():
    diary_entry = DiaryEntry('My Title', 'These are the contents this time.')
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == 'the contents'
