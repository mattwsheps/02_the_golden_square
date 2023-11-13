from lib.string_builder import *

"""
Test init
"""
def test_init():
    builder = StringBuilder()
    assert builder.str == ""

"""
Test add
"""
def test_add():
    builder = StringBuilder()
    builder.add('Hello')
    assert builder.str == "Hello"

def test_add_2():
    builder = StringBuilder()
    builder.add('Hello')
    builder.add(' Dave!')
    assert builder.str == "Hello Dave!"

"""
Test size
"""
def test_size():
    builder = StringBuilder()
    builder.add('Hello')
    builder.add(' Dave!')
    assert builder.size() == 11

"""
Test output
"""
def test_output():
    builder = StringBuilder()
    builder.add('Hello')
    builder.add(' Dave!')
    assert builder.output() == 'Hello Dave!'