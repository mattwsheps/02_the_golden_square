from lib.diary import *
from lib.diary_entry import *

"""
Given I add two diary entries
#all returns a list with those diary entries
"""
def test_add_two_diary_entries_and_list_them():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park.')
    entry2 = DiaryEntry('Tuesday', 'I went to the cinema.')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

"""
Given I add two diary entries
#count_words returns the sum of the number of words in all diary entries
"""
def test_add_two_diary_entries_and_count_words():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park.')
    entry2 = DiaryEntry('Tuesday', 'I went to the cinema.')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 10

"""
Given I add two diary entries both with entries that are 5 words long
and provide a reading speed of 2 wpm
#reading_time returns a reading time of 5 in mins to read all entries
"""
def test_reading_time_for_two_entries():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park.')
    entry2 = DiaryEntry('Tuesday', 'I went to the cinema.')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(2) == 5

"""
Given I add two entries, one too long and one short
and provide a wpm and minutes that would only allow me to read the short one
#find_best_entry_for_reading_time returns the short entry
"""
def test_find_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park for a very long time.')
    entry2 = DiaryEntry('Tuesday', 'I went to the cinema.')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2,3) == entry2

"""
Given I add two entries, both too long for the wpm and minutes provided
#find_best_entry_for_reading_time returns None
"""
def test_find_best_entry_for_reading_time_if_no_entries_suitable():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park for a very long time.')
    entry2 = DiaryEntry('Tuesday', 'I went to the park for a very long time.')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2,3) == None