from lib.task import *
import pytest

"""
Task constructs with a task.
"""
def test_task_initial_construction():
    task = Task('Walk the dog.')
    assert task.task == 'Walk the dog.'

"""
When I initialise with a task,
I can get that task back.
"""
def test_task_get_task_name():
    task = Task('Walk the dog.')
    assert task.task == 'Walk the dog.'

"""
When I initialise with a task,
the task's complete property is set to False.
"""
def test_task_intially_incomplete():
    task = Task('Walk the dog.')
    assert task.complete == False

"""
When I initialise with a task,
and I call #mark_complete,
the complete property is set to True
"""
def test_mark_complete():
    task = Task('Walk the dog.')
    task.mark_complete()
    assert task.complete == True

"""
When #mark_complete is called 
on an object that is already complete
raise an exception => 'This task is already complete.'
"""
def test_mark_complete_error():
    task = Task('Walk the dog.')
    task.mark_complete()
    with pytest.raises(Exception) as e:
        task.mark_complete()
    assert str(e.value) == 'This task is already complete.'