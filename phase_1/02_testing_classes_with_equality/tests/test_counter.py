from lib.counter import *

"""
Test the __init__ function
"""
def test_init():
    counter = Counter()
    assert counter.count == 0


"""
Test the add function
"""
def test_add_one_number():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_adding_two_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(4)
    assert counter.count == 9

"""
Test the report function
"""
def test_report_1():
    counter = Counter()
    counter.add(3)
    counter.add(7)
    assert counter.report() == "Counted to 10 so far."

def test_report_2():
    counter = Counter()
    counter.add(3)
    counter.add(7)
    counter.add(4)
    assert counter.report() == "Counted to 14 so far."