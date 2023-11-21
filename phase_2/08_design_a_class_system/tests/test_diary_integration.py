from lib.diary import *
from lib.diary_entry import *
from lib.phone_number_extractor import *
from lib.readable_entry_finder import *

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
Given I add three diary entries
Two of those with phone numbers
PhoneNumberExtractor's #extract_all will return a list of those two phone numbers
"""
def test_extract_two_phone_numbers():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park.')
    entry2 = DiaryEntry('Tuesday', 'Call 07000199299.')
    entry3 = DiaryEntry('Wednesday', 'Call 07501287905.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    extractor = PhoneNumberExtractor()
    assert extractor.extract_all(diary) == ['07000199299', '+447501287905']

"""
Given I add three diary entries
Two of those with the same phone number
PhoneNumberExtractor's #extract_all will return a list with no duplicates
"""
def test_extract_two_phone_numbers():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park.')
    entry2 = DiaryEntry('Tuesday', 'Call 07000199299.')
    entry3 = DiaryEntry('Wednesday', 'Call 07000199299.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    extractor = PhoneNumberExtractor()
    assert extractor.extract_all(diary) == ['07000199299']

"""
Given I add two entries, one too long and one short
and provide a wpm and minutes that would only allow me to read the short one
ReadableEntryFinder returns the short entry
"""
def test_find_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Monday', 'I went to the park for a very long time.')
    entry2 = DiaryEntry('Tuesday', 'I went to the cinema.')
    diary.add(entry1)
    diary.add(entry2)
    entry_finder = ReadableEntryFinder(2,3)
    assert entry_finder.find_entry(diary) == entry2