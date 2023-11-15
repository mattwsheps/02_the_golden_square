from lib.task_tracker import *
import pytest

"""
When no task has been added
#list_tasks returns an empty list
"""
def test_no_task_added():
    tracker = TaskTracker()
    assert tracker.list_tasks() == []

"""
When a task is added
#list_tasks returns the task in a list
"""
def test_task_added():
    tracker = TaskTracker()
    tracker.add('Make breakfast')
    assert tracker.list_tasks() == ['Make breakfast']

"""
When multiple tasks are added
#list_tasks returns all the tasks in a list
"""
def test_multiple_tasks_added():
    tracker = TaskTracker()
    tracker.add('Make breakfast')
    tracker.add('Make lunch')
    tracker.add('Make dinner')
    assert tracker.list_tasks() == ['Make breakfast', 'Make lunch', 'Make dinner']

"""
When multiple tasks are added
and mark one as complete
#list_tasks doesn't return the completed task
"""
def test_mark_complete():
    tracker = TaskTracker()
    tracker.add('Make breakfast')
    tracker.add('Make lunch')
    tracker.add('Make dinner')
    tracker.mark_complete(0)
    assert tracker.list_tasks() == ['Make lunch', 'Make dinner']

"""
When multiple tasks are added
and mark one as complete
#list_tasks doesn't return the completed task
"""
def test_mark_two_complete():
    tracker = TaskTracker()
    tracker.add('Make breakfast')
    tracker.add('Make lunch')
    tracker.add('Make dinner')
    tracker.mark_complete(0)
    tracker.mark_complete(1)
    assert tracker.list_tasks() == ['Make lunch']

"""
When an index is given that is outside of the index range
It raises the exception 'The given index is outside of the task lists range.'
"""
def test_index_invalid():
    tracker = TaskTracker()
    tracker.add('Make breakfast')
    with pytest.raises(Exception) as e:
        tracker.mark_complete(1)
    error_msg = str(e.value)
    assert error_msg == 'The given index is outside of the task lists range.'
