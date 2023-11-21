from lib.diary import *

"""
Initially,
#all returns an empty list
"""
def test_list_no_entries():
    diary = Diary()
    assert diary.all() == []