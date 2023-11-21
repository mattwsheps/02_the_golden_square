from lib.music_library import *
from unittest.mock import Mock

"""
Initially
#search returns an empty list
"""
def test_initially_no_tracks():
    library = MusicLibrary()
    assert library.search('The Beatles') == []

"""
When I add some tracks
They show up in the tracks list
"""
def test_tracks_added_to_list():
    library = MusicLibrary()
    track1 = Mock()
    track2 = Mock()
    track3 = Mock()
    library.add(track1)
    library.add(track2)
    library.add(track3)
    assert library.tracks == [track1, track2, track3]


"""
When I add two tracks
And I #search for a keyword
I get a list of tracks that match that keyword
"""
def test_searches_by_keyword():
    library = MusicLibrary()

    fake_track_that_matches = Mock()
    fake_track_that_matches.matches.return_value = True
    library.add(fake_track_that_matches)

    fake_track_that_doesnt_match = Mock()
    fake_track_that_doesnt_match.matches.return_value = False
    library.add(fake_track_that_doesnt_match)

    assert library.search('Yes') == [fake_track_that_matches]