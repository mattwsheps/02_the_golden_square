from lib.gratitudes import *

def test_initial():
    grat = Gratitudes()
    assert grat.format() == "Be grateful for: "

def test_add():
    grat = Gratitudes()
    grat.add('Friends')
    assert grat.format() == "Be grateful for: Friends"

def test_add_2():
    grat = Gratitudes()
    grat.add('Friends')
    grat.add('Family')
    assert grat.format() == "Be grateful for: Friends, Family"