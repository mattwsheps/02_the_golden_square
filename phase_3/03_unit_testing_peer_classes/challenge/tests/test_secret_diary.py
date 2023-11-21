from lib.secret_diary import *
import pytest
from unittest.mock import Mock

"""
When user tries to read when diary is locked
#read raises exception 'Go away!'
"""
def test_read_when_locked_with_mock():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == 'Go away!'


"""
When user tries to read when diary is unlocked
#read returns diary contents
"""
def test_read_when_unlocked_with_mock():
    diary = Mock()
    diary.read.return_value = 'I walked the dog.'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'I walked the dog.'

"""
When user tries to read when diary is relocked
#read returns diary contents
"""
def test_read_when_relocked_with_mock():
    diary = Mock()
    diary.read.return_value = 'I walked the dog.'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == 'Go away!'

