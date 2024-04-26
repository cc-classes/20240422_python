class MyProperty:
    def __init__(self, getter):
        self._getter = getter
        self._setter = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._getter(instance)

    def __set__(self, instance, value):
        if self._setter is None:
            raise AttributeError("can't set attribute")
        self._setter(instance, value)

    def setter(self, setter_func):
        self._setter = setter_func
        return self


# Usage
class MyClass:
    def __init__(self, first_name):
        self._first_name = first_name

    @MyProperty
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # def get_first_name(self):
    #     return self._first_name

    # def set_first_name(self, value):
    #     self._first_name = value


# my_prop = MyProperty(MyClass.get_first_name)
# my_prop.setter(MyClass.set_first_name)
# MyClass.first_name = my_prop


my_class = MyClass("Bob")
print(my_class.first_name)
my_class.first_name = "Alice"
print(my_class.first_name)
