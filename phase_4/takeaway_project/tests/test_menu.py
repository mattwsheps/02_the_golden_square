from lib.menu import *
from unittest.mock import Mock

"""
Initially
#show_menu returns an empty string
"""
def test_show_empty_menu():
    menu = Menu([])
    assert menu.show_menu() == ''

"""
Given a menu with a list of three dishes
When we want to see the menu
#show_menu returns a list of strings with the dishes and their prices
"""
def test_menu_intialised_with_three_dishes_and_show_menu_mock():
    dish1 = Mock()
    dish1.name = 'Chicken Tikka Masala'
    dish1.price = 12
    dish1.cooking_time = 30

    dish2 = Mock()
    dish2.name = 'Lamb Bhuna'
    dish2.price = 15
    dish2.cooking_time = 45

    dish3 = Mock()
    dish3.name = 'Poppadoms'
    dish3.price = 3
    dish3.cooking_time = 5
    menu = Menu([dish1, dish2, dish3])
    assert menu.show_menu() == 'Chicken Tikka Masala - £12.00\nLamb Bhuna - £15.00\nPoppadoms - £3.00'

"""
Given a menu with an empty list
When we add two dishes
And want to see the menu
#show_menu returns those two dishes and their prices
"""
def test_add_two_dishes_to_an_empty_menu_mock():
    dish1 = Mock()
    dish1.name = 'Chicken Tikka Masala'
    dish1.price = 12
    dish1.cooking_time = 30

    dish2 = Mock()
    dish2.name = 'Lamb Bhuna'
    dish2.price = 15
    dish2.cooking_time = 45

    menu = Menu([])
    menu.add_to_menu(dish1)
    menu.add_to_menu(dish2)
    assert menu.show_menu() == 'Chicken Tikka Masala - £12.00\nLamb Bhuna - £15.00'