# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE
class TaskTracker:
    def __init__(self):
        """
        Side effects: stores a list of the incomplete tasks
        """

    def add(self, task):
        """
        Parameters:
            task: a string representing a task
        Side effects:
            Adds the given task to a list
        """
        pass

    def list_tasks(self):
        """
        Returns:
            A list of the incomplete tasks.
        """
        pass

    def mark_complete(self, index):
        """
        Parameters:
            index: an integer representing the task to complete
        Side effects:
            removes the completed task from the list
        """
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
# EXAMPLE

"""
When no task has been added
#list_tasks returns an empty list
"""
tracker = TaskTracker()
tracker.list_tasks() # => []

"""
When a task is added
#list_tasks returns the task in a list
"""
tracker = TaskTracker()
tracker.add('Make breakfast')
tracker.list_tasks() # => ['Make breakfast']

"""
When multiple tasks are added
#list_tasks returns all the tasks in a list
"""
tracker = TaskTracker()
tracker.add('Make breakfast')
tracker.add('Make lunch')
tracker.add('Make dinner')
tracker.list_tasks() # => ['Make breakfast', 'Make lunch', 'Make dinner']

"""
When multiple tasks are added
and mark one as complete
#list_tasks doesn't return the completed task
"""
tracker = TaskTracker()
tracker.add('Make breakfast')
tracker.add('Make lunch')
tracker.add('Make dinner')
tracker.mark_complete(0)
tracker.list_tasks() # => ['Make lunch', 'Make dinner']

"""
When multiple tasks are added
and mark one as complete
#list_tasks doesn't return the completed task
"""
tracker = TaskTracker()
tracker.add('Make breakfast')
tracker.add('Make lunch')
tracker.add('Make dinner')
tracker.mark_complete(0)
tracker.mark_complete(1)
tracker.list_tasks() # => ['Make lunch']

"""
When an index is given that is outside of the index range
It raises the exception 'The given index is outside of the task lists range.'
"""
tracker = TaskTracker()
tracker.add('Make breakfast')
tracker.mark_complete(1) # => 'The given index is outside of the task lists range.'


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```
