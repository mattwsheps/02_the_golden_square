# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:
    def __init__(self):
        """
        Parameters:
            entries: a list of DiaryEntry objects
        """
        pass

    def add(self, entry):
        """
        Parameters:
            entry: an instance of DiaryEntry
        Side effects:
            adds the entry to the list of entries
        """
        pass

    def all(self):
        """
        Returns:
            a list of all added entries
        """
        pass


class DiaryEntry:
    def __init__(self, title, contents):
        """
        Parameters:
            title: a string representing the title of the diary entry
            contents: a string representing the contents of the diary entry
            contents_list: a list where each element is a word in the      contents string
        """
        pass

    def count_words(self):
        """
        Returns:
            an integer representing the number of words in the contents
        """
        pass

class ReadableEntryFinder:
    def __init__(self, wpm, minutes):
        """
        Parameters:
            wpm: an int representing reading speed in words per min
            minutes: an int representing the minutes available to the reader
        """
        pass

    def find_entry(diary):
        """
        Parameters:
            diary: an instance of a diary
        Returns:
            an entry to read based on reading speed and time available
        """
        pass

class PhoneNumberExtractor:
    def __init__(self):
        pass

    def extract_all(self):
        """
        Returns:
            A list of strings representing phone numbers that can be found in the diary entries
        """
        pass

class TaskList:
    def __init__(self):
        """
        Side effects:
            Stores a list of strings representing tasks
        """
        pass

    def add(self, task):
        """
        Parameters:
            task: a string representing a task to complete
        Side effects:
            Adds the task to the list of tasks
        """
        pass

    def all(self):
        """
        Returns:
            A list of all added tasks
        """
        pass

class Task:
    def __init__(self, task):
        """
        Parameters:
            task: a string representing a task
        """
        pass


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

````python
# EXAMPLE



## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Initially, diary has no entries
"""
````

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
