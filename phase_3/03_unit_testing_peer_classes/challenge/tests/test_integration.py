from lib.diary import *
from lib.secret_diary import *
import pytest

"""
When user tries to read when diary is locked
#read raises exception 'Go away!'
"""
def test_read_when_locked():
    diary = Diary('walk the dog.')
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == 'Go away!'


"""
When user tries to read when diary is unlocked
#read returns diary contents
"""
def test_read_when_unlocked():
    diary = Diary('I walked the dog.')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'I walked the dog.'

"""
When user tries to read when diary is relocked
#read returns diary contents
"""
def test_read_when_relocked():
    diary = Diary('I walked the dog.')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == 'Go away!'