from lib.order_manager import *
from unittest.mock import Mock

"""
Given an empty menu
OrderManager#show_order returns an empty list
"""
def test_empty_menu_show_order_mock():
    menu = Mock()
    order_manager = OrderManager(menu)
    assert order_manager.show_order() == ''

"""
Given a menu
When we add the 2nd dish to our order
And want to see our order
OrderManager#show_order returns a string representing an itemised receipt with a grand total
"""
def test_add_2nd_dish_to_order_and_show_mock():
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

    menu = Mock(dish_list=[dish1, dish2, dish3])

    order_manager = OrderManager(menu)
    order_manager.add_to_order(2)
    assert order_manager.show_order() == 'Lamb Bhuna - £15.00\nGrand Total - £15.00'

"""
Given a menu
When we add the 2nd and 3rd dish to our order
And want to see our order
OrderManager#show_order returns a string representing an itemised receipt with a grand total
"""
def test_add_2nd_and_3rd_dish_to_order_and_show_mock():
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

    menu = Mock(dish_list=[dish1, dish2, dish3])
    order_manager = OrderManager(menu)
    order_manager.add_to_order(2)
    order_manager.add_to_order(3)
    assert order_manager.show_order() == 'Lamb Bhuna - £15.00\nPoppadoms - £3.00\nGrand Total - £18.00'

"""
Given a menu and that the time is 12pm
When we add the 2nd and 3rd dish to our order both with cooking times of 45 mins and 5 mins respectively
And given the delivery itself takes 15 mins
OrderManager#calculate_delivery_time returns a time of 13:00
"""
def test_calculate_order_with_1_hour_delivery_time_mock():
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

    menu = Mock(dish_list=[dish1, dish2, dish3])
    order_manager = OrderManager(menu)
    order_manager.add_to_order(2)
    order_manager.add_to_order(3)

    datetime_mock = Mock(name="datetime")
    datetime_mock.now.return_value = datetime(2023, 11, 21, 12, 00, 00)

    assert order_manager.calculate_delivery_time(7.5, datetime_mock) == '13:00'

"""
Given that the delivery time is estimated to be 16:56
#confirmation_message returns a string saying 
"Thank you! Your order was placed and will be delivered before 16:56"
"""
def test_create_confimation_message_mock():
    menu = Mock()
    order_manager = OrderManager(menu)
    assert order_manager.confirmation_message('16:56') == "Thank you! Your order was placed and will be delivered before 16:56"

"""
Given a menu and that the time is 12pm
When we add the 2nd and 3rd dish to our order both with cooking times of 45 mins and 5 mins respectively
And given the delivery itself takes 15 mins
when given #calculate_delivery_time
#create_confirmation_message returns a string saying 
"Thank you! Your order was placed and will be delivered before 13:00"
"""
def test_confirmation_message_with_1_hour_delivery_time_mock():
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

    menu = Mock(dish_list=[dish1, dish2, dish3])
    order_manager = OrderManager(menu)
    order_manager.add_to_order(2)
    order_manager.add_to_order(3)

    datetime_mock = Mock(name="datetime")
    datetime_mock.now.return_value = datetime(2023, 11, 21, 12, 00, 00)

    order_manager.confirmation_message(order_manager.calculate_delivery_time(7.5, datetime_mock)) == "Thank you! Your order was placed and will be delivered before 13:00"

"""
Given an empty menu, a phone number of '+44700000000', a confirmation message of 'Hi'
#place_order will send a text with that phone number and message
"""

def test_place_order():
    menu = Mock()
    text_sender_mock = Mock()
    text_sender_mock.send_text.return_value = True

    order_manager = OrderManager(menu)

    result = order_manager.place_order(text_sender_mock, '+44700000000', 'Hi')

    text_sender_mock.send_text.assert_called_with('+44700000000', 'Hi')

    assert result