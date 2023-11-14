from lib.task_tracker import *
import pytest

"""
Given a string with #TODO at the start
It returns True
"""
def test_todo_at_start():
    result = task_tracker("#TODO Complete this task.")
    assert result == True

"""
Given a string with #TODO in the middle
It returns True
"""
def test_todo_in_middle():
    result = task_tracker("To-do list: #TODO Complete this task.")
    assert result == True

"""
Given a string with #TODO at the end
It returns True
"""
def test_todo_at_end():
    result = task_tracker("To-do list: Complete this task. #TODO")
    assert result == True

"""
Given a string that doesn't include #TODO
It returns False
"""
def test_no_todo():
    result = task_tracker("To-do list: Complete this task.")
    assert result == False

"""
Given an empty string
It raises the exception: "Input text cannot be empty."
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        task_tracker("")
    error_msg = str(e.value)
    assert error_msg == "Input text cannot be empty."


