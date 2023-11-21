from lib.task_list import *

"""
Initially, #incomplete returns an empty list
"""
def test_initially_incomplete_empty_list():
    task_list = TaskList()
    assert task_list.incomplete() == []

"""
Initially, #complete returns an empty list
"""
def test_initially_complete_empty_list():
    task_list = TaskList()
    assert task_list.complete() == []