class Dish:
    def __init__(self, name, price, cooking_time):
        """
        Parameters:
            name: a string represnting the name of the dish
            price: a float representing the price in GBP
            cooking_time: an int representing cooking time in minutes
        """
        self.name = name
        self.price = price
        self.cooking_time = cooking_time