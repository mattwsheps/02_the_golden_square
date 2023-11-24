# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class MusicLibrary:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Track objects that have titles that include the keyword
        pass # No code here yet


class Track:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
#--- MENU INTEGRATION ---#

"""
Given a menu with a list of three dishes
When we request to see the menu
#show_menu returns a string with the dishes and their prices
"""
dish1 = Dish('Chicken Tikka Masala', 12, 30)
dish2 = Dish('Lamb Bhuna', 15, 45)
dish3 = Dish('Poppadoms', 3, 5)
menu = Menu([dish1, dish2, dish3])
menu.show_menu()    # =>    'Chicken Tikka Masala - £12.00
                    #       Lamb Bhuna - £15.00
                    #       Poppadoms - £3.00'

"""
Given a menu with an empty list
When we add two dishes
And want to see the menu
#show_menu returns those two dishes and their prices
"""
dish1 = Dish('Chicken Tikka Masala', 12, 30)
dish2 = Dish('Lamb Bhuna', 15, 45)
menu = Menu([])
menu.add_to_menu(dish1)
menu.add_to_menu(dish2)
menu.show_menu()    # =>    'Chicken Tikka Masala - £12.00
                    #       Lamb Bhuna - £15.00'

#--- ORDER MANAGER INTEGRATION ---#
"""
Given an empty menu
OrderManager#show_order returns an empty string
"""
menu = Menu([])
order_manager = OrderManager(menu)
order_manager.show_order() # => ''

"""
Given a menu
When we add the 2nd dish to our order
And want to see our order
OrderManager#show_order returns a string representing an itemised receipt with a grand total
"""
dish1 = Dish('Chicken Tikka Masala', 12, 30)
dish2 = Dish('Lamb Bhuna', 15, 45)
dish3 = Dish('Poppadoms', 3, 5)
menu = Menu([dish1, dish2, dish3])
order_manager = OrderManager(menu)
order_manager.add_to_order(2)
order_manager.show_order()  # =>    'Lamb Bhuna - £15.00
                            #       Grand Total - £15.00'

"""
Given a menu
When we add the 2nd and 3rd dish to our order
And want to see our order
OrderManager#show_order returns a string representing an itemised receipt with a grand total
"""
dish1 = Dish('Chicken Tikka Masala', 12, 30)
dish2 = Dish('Lamb Bhuna', 15, 45)
dish3 = Dish('Poppadoms', 3, 5)
menu = Menu([dish1, dish2, dish3])
order_manager = OrderManager(menu)
order_manager.add_to_order(2)
order_manager.add_to_order(3)
order_manager.show_order()  # =>    'Lamb Bhuna - £15.00
                            #       Poppadoms - £3.00
                            #       Grand Total - £18.00'

"""
Given a menu and that the time is 12pm
When we add the 2nd and 3rd dish to our order both with cooking times of 45 mins and 5 mins respectively
And given the delivery itself takes 15 mins
OrderManager#calculate_delivery_time returns a time of 13:00
"""
dish1 = Dish('Chicken Tikka Masala', 12, 30)
dish2 = Dish('Lamb Bhuna', 15, 45)
dish3 = Dish('Poppadoms', 3, 5)
menu = Menu([dish1, dish2, dish3])
order_manager = OrderManager(menu)
order_manager.add_to_order(2)
order_manager.add_to_order(3)
order_manager.calculate_delivery_time() # =>  '13:00'

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
"""
Initially
#show_menu returns an empty list
"""
menu = Menu([])
menu.show_menu() # => []

"""
Dish is constructed with a name, price and cooking_time
"""
dish1 = Dish('Chicken Tikka Masala', 12, 30)
dish1.name # => 'Chicken Tikka Masala'
dish1.price # => 12
dish1.cooking_time # => 30

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
