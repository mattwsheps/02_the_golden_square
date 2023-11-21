from lib.track import *

"""
Track is constructed with a title and artist
"""
def test_track_construction():
    track = Track('Let it be', 'The Beatles')
    assert track.artist == 'The Beatles'
    assert track.title == 'Let it be'

"""
When given a keyword string that matches the full title
#matches returns True
"""
def test_keyword_matches():
    track = Track('Let it be', 'The Beatles')
    assert track.matches('Let it be')

"""
When given a keyword string that matches part of the title
#matches returns True
"""
def test_keyword_matches():
    track = Track('Let it be', 'The Beatles')
    assert track.matches('Let it')

"""
When given a keyword string that matches the full artist
#matches returns True
"""
def test_keyword_matches():
    track = Track('Let it be', 'The Beatles')
    assert track.matches('The Beatles')

"""
When given a keyword string that matches part of the artist
#matches returns True
"""
def test_keyword_matches():
    track = Track('Let it be', 'The Beatles')
    assert track.matches('Beatles')

"""
When given a keyword string that doesn't match the title or artist
#matches returns False
"""
def test_keyword_doesnt_match():
    track = Track('Let it be', 'The Beatles')
    assert not track.matches('Hey Jude')