from lib.music_tracker import *
import pytest

"""
Given no track
#show_tracks returns an empty list
"""
def test_no_track_added():
    tracker = MusicTracker()
    assert tracker.show_tracks() == []

"""
If one track is added
#show_tracks returns the track in a list
"""
def test_add_track():
    tracker = MusicTracker()
    tracker.add('Let it be')
    assert tracker.show_tracks() == ['Let it be']

"""
If multiple tracks are added
#show_tracks returns all the tracks in a list
"""
def test_multiple_tracks_added():
    tracker = MusicTracker()
    tracker.add('Let it be')
    tracker.add('Hey Jude')
    tracker.add('Come together')
    tracker.show_tracks() == ['Let it be', 'Hey Jude', 'Come together']

"""
If an empty string is added
It raises an exception 'Input string cannot be empty.'
"""
def test_empty_string_added():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.add('')
    error_msg = str(e.value)
    assert error_msg == 'Input string cannot be empty.'

"""
If given input is not a string
It raises an exception 'Input must be a string.'
"""
def test_not_a_string_added():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.add(3)
    error_msg = str(e.value)
    assert error_msg == 'Input must be a string.'