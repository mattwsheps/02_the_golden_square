from lib.music_library import *
from lib.track import *

"""
When I add multiple tracks
They are reflected in the tracks list
"""
def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track1 = Track('Let it be', 'The Beatles')
    track2 = Track('Californication', 'Red Hot Chili Peppers')
    library.add(track1)
    library.add(track2)
    assert library.tracks == [track1, track2]

"""
When I add two tracks
And I #search for a keyword
I get a list of tracks that match that keyword
"""
def test_searches_by_keyword():
    library = MusicLibrary()
    track1 = Track('Let it be', 'The Beatles')
    track2 = Track('Californication', 'Red Hot Chili Peppers')
    library.add(track1)
    library.add(track2)
    assert library.search('Red Hot') == [track2]