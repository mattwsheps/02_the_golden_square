from lib.dish import *

"""
Dish is constructed with a name, price and cooking_time
"""
def test_dish_construction():
    dish1 = Dish('Chicken Tikka Masala', 12, 30)
    assert dish1.name == 'Chicken Tikka Masala'
    assert dish1.price == 12
    assert dish1.cooking_time == 30