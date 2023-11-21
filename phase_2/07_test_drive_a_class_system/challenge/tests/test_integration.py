from lib.todo import *
from lib.todo_list import *

"""
Given two incomplete todo objects are added
#incomplete returns the two todo objects in a list
"""
def test_add_two_todo_return_incomplete():
    todo_list = TodoList()
    task1 = Todo('Wash the dishes.')
    task2 = Todo('Walk the dog.')
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.incomplete() == [task1, task2]

"""
Given two incomplete todo objects are added
and one is marked complete
#complete returns the one that is complete in a list
"""
def test_complete():
    todo_list = TodoList()
    task1 = Todo('Wash the dishes.')
    task2 = Todo('Walk the dog.')
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    assert todo_list.complete() == [task1]

"""
Given two incomplete todo objects are added
and one is marked complete
#incomplete returns the one that is incomplete in a list
"""
def test_incomplete_when_one_task_complete():
    todo_list = TodoList()
    task1 = Todo('Wash the dishes.')
    task2 = Todo('Walk the dog.')
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    assert todo_list.incomplete() == [task2]

"""
Given three todo objects are added
#give_up marks them all as complete
and #complete displays them all in a list
"""
def test_give_up_when_all_incomplete():
    todo_list = TodoList()
    task1 = Todo('Wash the dishes.')
    task2 = Todo('Walk the dog.')
    task3 = Todo('Go to the shops.')
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    todo_list.give_up()
    assert todo_list.complete() == [task1, task2, task3]

"""
Given three todo objects are added
and one is marked as complete
#give_up marks them all as complete
and #complete displays them all in a list
"""
def test_give_up_when_some_incomplete():
    todo_list = TodoList()
    task1 = Todo('Wash the dishes.')
    task2 = Todo('Walk the dog.')
    task3 = Todo('Go to the shops.')
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    task2.mark_complete()
    todo_list.give_up()
    assert todo_list.complete() == [task1, task2, task3]