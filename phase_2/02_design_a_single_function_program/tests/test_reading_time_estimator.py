from lib.reading_time_estimator import *
import pytest

"""
Given a text of 200 words
It will return a reading time of 1.0
"""
def test_with_200_words():
    words_200 = (" ").join(["word" for i in range(200)])
    result = reading_time_estimator(words_200)
    assert result == 1.0

"""
Given a text of 400 words
It will return a reading time of 2.0
"""
def test_with_400_words():
    words_400 = (" ").join(["word" for i in range(400)])
    result = reading_time_estimator(words_400)
    assert result == 2.0

"""
Given a text of 300 words
It will return 1
"""
def test_with_300_words():
    words_300 = (" ").join(["word" for i in range(300)])
    result = reading_time_estimator(words_300)
    assert result == 1.5

"""
Given an empty string
It will raise an error
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        reading_time_estimator("")
    error_msg = str(e.value)
    assert error_msg == "Can't estimate reading time for an empty text."
