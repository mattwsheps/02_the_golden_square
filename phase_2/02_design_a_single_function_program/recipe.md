# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def grammar_improver(text):
    """
    A function that validates if a text starts with a capital letter and ends with a suitable-ending punctuation mark

    Parameters:
        text: a string of the text to be verified

    Returns
        text_valid: A boolean which is True if the text is grammatically valid and False if not.
    """
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given a text that doesn't start with a capital letter and doesn't end with a suitable punctuation mark
It will return False
"""

"""
Given a text that starts with a capital letter and ends with a suitable punctuation mark
It will return True
"""

"""
Given a text that doesn't start with a capital letter and ends with a suitable punctuation mark
It will return False
"""

"""
Given a text that starts with a capital letter and doesn't end with a suitable punctuation mark
It will return False
"""

"""
Given an empty string
It will raise the exception "You cannot input an empty string."
"""


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

```

Ensure all test function names are unique, otherwise pytest will ignore them!
