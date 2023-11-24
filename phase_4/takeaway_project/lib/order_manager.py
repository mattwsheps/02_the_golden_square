from datetime import datetime, timedelta

class OrderManager:
    """
    Parameters:
        menu: An instance of a menu
    
    Attributes:
        _order_list: A list of the Dish instances in the order.
    """
    def __init__(self, menu):
        self._menu = menu
        self._order_list = []

    def add_to_order(self, dish_no):
        """
        Parameters:
            dish_no: An int representing the dish's place in the menu list
        Side effects:
            Adds dish to the order list
        """
        self._order_list.append(self._menu.dish_list[dish_no-1])
        

    def show_order(self):
        """
        Returns: 
            A string representing an itemised receipt with a grand total
        """
        order_string = ''
        grand_total = 0
        for dish in self._order_list:
            order_string += f"{dish.name} - £{format(dish.price, '.2f')}\n"
            grand_total += dish.price
        if self._order_list:
            order_string += f"Grand Total - £{format(grand_total, '.2f')}"
        return order_string

    def calculate_delivery_time(self, distance, timer):
        """
        Parameters:
            distance: An float representing the user's distance from the restaurant in miles
        Returns:
            A string representing expected delivery time
        """
        current_datetime = timer.now()
        cooking_time_list = [dish.cooking_time for dish in self._order_list]

        delivery_duration = timedelta(hours=distance/30)
        delivery_duration += timedelta(minutes=max(cooking_time_list))
        
        delivery_datetime = current_datetime + delivery_duration

        return delivery_datetime.strftime('%H:%M')
    
    def confirmation_message(self, delivery_time):
        """
        Parameters:
            delivery_time: a string representing the estimated time of delivery
        Returns:
            a string representing the confirmation of the order with an estimated delivery time.
        """
        return f"Thank you! Your order was placed and will be delivered before {delivery_time}"

    def place_order(self, text_sender, phone_no, confirmation_message):
        """ 
        Parameters:
            text_sender: an instance of TextSender
            phone_no: a string representing a phone number
            confirmation_message: a string representing the confirmation of the order with an estimated delivery time.
        Returns:
            Sends the string as an SMS to the user stating the delivery time
        """
        return text_sender.send_text(phone_no, confirmation_message)
    
