from lib.dish import *
from lib.menu import *
from lib.order_manager import *
from unittest.mock import Mock

"""
Given an empty menu
OrderManager#show_order returns an empty list
"""
def test_empty_menu_show_order():
    menu = Menu([])
    order_manager = OrderManager(menu)
    assert order_manager.show_order() == ''

"""
Given a menu
When we add the 2nd dish to our order
And want to see our order
OrderManager#show_order returns a string representing an itemised receipt with a grand total
"""
def test_add_2nd_dish_to_order_and_show():
    dish1 = Dish('Chicken Tikka Masala', 12, 30)
    dish2 = Dish('Lamb Bhuna', 15, 45)
    dish3 = Dish('Poppadoms', 3, 5)
    menu = Menu([dish1, dish2, dish3])
    order_manager = OrderManager(menu)
    order_manager.add_to_order(2)
    assert order_manager.show_order() == 'Lamb Bhuna - £15.00\nGrand Total - £15.00'

"""
Given a menu
When we add the 2nd and 3rd dish to our order
And want to see our order
OrderManager#show_order returns a string representing an itemised receipt with a grand total
"""
def test_add_2nd_and_3rd_dish_to_order_and_show():
    dish1 = Dish('Chicken Tikka Masala', 12, 30)
    dish2 = Dish('Lamb Bhuna', 15, 45)
    dish3 = Dish('Poppadoms', 3, 5)
    menu = Menu([dish1, dish2, dish3])
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
def test_calculate_order_with_1_hour_delivery_time():
    dish1 = Dish('Chicken Tikka Masala', 12, 30)
    dish2 = Dish('Lamb Bhuna', 15, 45)
    dish3 = Dish('Poppadoms', 3, 5)
    menu = Menu([dish1, dish2, dish3])
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
    menu = Menu([])
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
def test_confirmation_message_with_1_hour_delivery_time():
    dish1 = Dish('Chicken Tikka Masala', 12, 30)
    dish2 = Dish('Lamb Bhuna', 15, 45)
    dish3 = Dish('Poppadoms', 3, 5)
    menu = Menu([dish1, dish2, dish3])
    order_manager = OrderManager(menu)
    order_manager.add_to_order(2)
    order_manager.add_to_order(3)

    datetime_mock = Mock(name="datetime")
    datetime_mock.now.return_value = datetime(2023, 11, 21, 12, 00, 00)

    order_manager.confirmation_message(order_manager.calculate_delivery_time(7.5, datetime_mock)) == "Thank you! Your order was placed and will be delivered before 13:00"

"""
Given a menu and that the time is 12pm
When we add the 2nd and 3rd dish to our order both with cooking times of 45 mins and 5 mins respectively
And given the delivery itself takes 15 mins
when given #calculate_delivery_time
#send_text sends a string via SMS using twilio saying 
"Thank you! Your order was placed and will be delivered before 13:00"
"""

def test_place_order_with_delivery_time_1pm():
    dish1 = Dish('Chicken Tikka Masala', 12, 30)
    dish2 = Dish('Lamb Bhuna', 15, 45)
    dish3 = Dish('Poppadoms', 3, 5)
    menu = Menu([dish1, dish2, dish3])
    order_manager = OrderManager(menu)
    order_manager.add_to_order(2)
    order_manager.add_to_order(3)

    datetime_mock = Mock(name="datetime")
    datetime_mock.now.return_value = datetime(2023, 11, 21, 12, 00, 00)

    text_sender_mock = Mock(name='text_sender')
    text_sender_mock.send_text.return_value = True

    order_confirmation_message = order_manager.confirmation_message(order_manager.calculate_delivery_time(7.5, datetime_mock))

    order_manager.place_order(text_sender_mock, '+44700000000', order_confirmation_message)

    text_sender_mock.send_text.assert_called_with('+44700000000', order_confirmation_message)

    assert order_manager.place_order
