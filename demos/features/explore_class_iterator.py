class Product:
    def __init__(self, id, name, price):
        # double-underscore prefix marks and attribute as private
        # hide information in a class is called encapsulation
        self.__id = id
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__id} {self.__name} {self.__price}"

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name.upper()

    @property
    def price(self):
        return self.__price


class CartIterator:
    def __init__(self, items):
        self.__items = items
        self.__current_index = -1

    # magic method - is a method connected into Python's operator system
    def __next__(self):
        self.__current_index += 1
        if self.__current_index >= len(self.__items):
            raise StopIteration()
        return self.__items[self.__current_index]


class Cart:
    def __init__(self):
        self.__items = []

    def add_item(self, product):
        self.__items.append(product)

    def __iter__(self):
        return CartIterator(self.__items)


cart = Cart()
cart.add_item(Product(1, "apples", 2.34))
cart.add_item(Product(2, "oranges", 3.50))
cart.add_item(Product(3, "plums", 5.00))

# mini lab exercise

# use the code above, iterate over the shopping cart
# and display the product names

# for-in loop will call iter(cart) -> instance of CartIterator
# on each iteration it calls next(cart_iterator) -> an item in the list
for item in cart:
    print(item.name)
