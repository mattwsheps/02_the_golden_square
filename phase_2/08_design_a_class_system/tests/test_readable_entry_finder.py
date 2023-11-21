from lib.readable_entry_finder import *

"""
ReadableEntryFinder constructed with a wpm and minutes
"""
def test_entry_finder_initial_construction():
    entry_finder = ReadableEntryFinder(2,10)
    assert entry_finder.wpm == 2
    assert entry_finder.minutes == 10