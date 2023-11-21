from lib.task import *
from lib.task_list import *

"""
Given two incomplete task objects are added
#incomplete returns the two task objects in a list
"""
def test_add_two_task_return_incomplete():
    task_list = TaskList()
    task1 = Task('Wash the dishes.')
    task2 = Task('Walk the dog.')
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.incomplete() == [task1, task2]

"""
Given two incomplete task objects are added
and one is marked complete
#complete returns the one that is complete in a list
"""
def test_complete():
    task_list = TaskList()
    task1 = Task('Wash the dishes.')
    task2 = Task('Walk the dog.')
    task_list.add(task1)
    task_list.add(task2)
    task1.mark_complete()
    assert task_list.complete() == [task1]

"""
Given two incomplete task objects are added
and one is marked complete
#incomplete returns the one that is incomplete in a list
"""
def test_incomplete_when_one_task_complete():
    task_list = TaskList()
    task1 = Task('Wash the dishes.')
    task2 = Task('Walk the dog.')
    task_list.add(task1)
    task_list.add(task2)
    task1.mark_complete()
    assert task_list.incomplete() == [task2]

"""
Given three task objects are added
#give_up marks them all as complete
and #complete displays them all in a list
"""
def test_give_up_when_all_incomplete():
    task_list = TaskList()
    task1 = Task('Wash the dishes.')
    task2 = Task('Walk the dog.')
    task3 = Task('Go to the shops.')
    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    task_list.give_up()
    assert task_list.complete() == [task1, task2, task3]

"""
Given three task objects are added
and one is marked as complete
#give_up marks them all as complete
and #complete displays them all in a list
"""
def test_give_up_when_some_incomplete():
    task_list = TaskList()
    task1 = Task('Wash the dishes.')
    task2 = Task('Walk the dog.')
    task3 = Task('Go to the shops.')
    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    task2.mark_complete()
    task_list.give_up()
    assert task_list.complete() == [task1, task2, task3]