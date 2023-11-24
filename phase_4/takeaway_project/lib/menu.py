class Menu():
    """
    Parameters:
        dish_list: a list of Dish instances
    """
    def __init__(self, dish_list):
        self.dish_list = dish_list

    def show_menu(self):
        """
        Returns:
            a string representing the dish names and prices
        """
        menu_string = ''
        for dish in self.dish_list:
            menu_string += f"{dish.name} - £{format(dish.price, '.2f')}\n"
        return menu_string[:-1]

    def add_to_menu(self, dish):
        """
        Parameters:
            dish: an instance of Dish
        Side effects:
            Adds the dish to the list of dishes
        """
        self.dish_list.append(dish)