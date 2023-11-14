# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def task_tracker(text):
    """
    A function that checks if '#TODO' is in a given text

    Parameters:
        text: a string of text

    Returns:
        A boolean where True means #TODO is in the text and False means it isn't
    """
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given a string with #TODO at the start
It returns True
"""
task_tracker("#TODO Complete this task.")
# => True

"""
Given a string with #TODO in the middle
It returns True
"""
task_tracker("To-do list: #TODO Complete this task.")
# => True

"""
Given a string with #TODO at the end
It returns True
"""
task_tracker("To-do list: Complete this task. #TODO")
# => True

"""
Given a string that doesn't include #TODO
It returns False
"""
task_tracker("To-do list: Complete this task.")
# => False

"""
Given an empty string
It raises the exception: "Input text cannot be empty"
"""
task_tracker("")
# => False

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

```

Ensure all test function names are unique, otherwise pytest will ignore them!
