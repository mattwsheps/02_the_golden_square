from lib.diary import *
import pytest

"""
Initially,
#all returns an empty list
"""
def test_list_no_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially,
#count_words returns 0
"""
def test_count_no_entries():
    diary = Diary()
    assert diary.count_words() == 0

"""
Initially,
#reading_time raises an error
"""
def test_reading_time_no_entries_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    assert str(e.value) == 'No entries added yet.'

"""
Initially,
#find_best_entry_for_reading_time raises an error
"""
def test_find_best_entry_for_reading_time_no_entries_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2,3)
    assert str(e.value) == 'No entries added yet.'

