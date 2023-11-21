from lib.task_formater import TaskFormatter
from lib.task import Task


def test_int_format_incomplete_task():
    task = Task('walk the dog')
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "-[ ] walk the dog"


def test_int_format_complete_task():
    task = Task('walk the dog')
    task.mark_complete()
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "-[x] walk the dog"



































# def test_format_complet_task_int():
#     # - [x] Task title
#     task = Task('walk the dog')
#     task_list = TaskList()
#     task_list.add(task)
#     task.mark_complete()
#     task_formatter = TaskFormatter(task)
#     formatted_task = task_formatter.format()
#     assert str(formatted_task) == f'-[x] {task.title}'




# # def test_format_incomplete_task():
# #         # If the task is not complete, the format is:
# #         # - [ ] Task title 
# #         task = Task('walk the dog')
# #         task_formatter = TaskFormatter(task)
# #         formatted_task = task_formatter.format()
# #         assert str(formatted_task) == f'-[ ] {task.title}'