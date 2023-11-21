from lib.todo import *
import pytest

"""
When I initialise with a task,
I can get that task back.
"""
def test_todo_get_task_name():
    task = Todo('Walk the dog.')
    assert task.task == 'Walk the dog.'

"""
When I initialise with a task,
the task's complete property is set to False.
"""
def test_todo_intially_incomplete():
    task = Todo('Walk the dog.')
    assert task.complete == False

"""
When I initialise with a task,
and I call #mark_complete,
the complete property is set to True
"""
def test_mark_complete():
    task = Todo('Walk the dog.')
    task.mark_complete()
    assert task.complete == True

"""
When #mark_complete is called 
on an object that is already complete
raise an exception => 'This task is already complete.'
"""
def test_mark_complete_error():
    task = Todo('Walk the dog.')
    task.mark_complete()
    with pytest.raises(Exception) as e:
        task.mark_complete()
    assert str(e.value) == 'This task is already complete.'