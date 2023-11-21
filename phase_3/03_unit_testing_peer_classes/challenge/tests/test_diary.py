from lib.diary import *

"""
Diary constructed with contents
"""
def test_diary_construction():
    diary = Diary('Walk the dog.')
    assert diary.read() == 'Walk the dog.'