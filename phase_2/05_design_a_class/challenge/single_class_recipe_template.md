# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class MusicTracker():
    def __init__(self):
        """
        Side effects:
            Stores the added tracks in a list
        """
        pass

    def add(self, track):
        """
        Parameters:
            track: a string representing the name of a track that has been listened to

        Side effects:
            Adds the given track to a list
        """
        pass

    def show_tracks(self):
        """
        Returns:
            the list of tracks that have been listened to
        """
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
"""
Given no track
#show_tracks returns an empty list
"""
tracker = MusicTracker()
tracker.show_tracks() # => []

"""
If one track is added
#show_tracks returns the track in a list
"""
tracker = MusicTracker()
tracker.add('Let it be')
tracker.show_tracks() # => ['Let it be']

"""
If multiple tracks are added
#show_tracks returns all the tracks in a list
"""
tracker = MusicTracker()
tracker.add('Let it be')
tracker.add('Hey Jude')
tracker.add('Come together')
tracker.show_tracks() # => ['Let it be', 'Hey Jude', 'Come together']

"""
If an empty string is added
It raises an exception 'Input string cannot be empty.'
"""
tracker = MusicTracker()
tracker.add('') # => 'Input string cannot be empty.'

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
