from __future__ import annotations


class Person:
    def __init__(self, fn: str, ln: str) -> None:
        self.__first_name = fn
        self.__last_name = ln

    @staticmethod
    def parse_full_name(full_name_str: str) -> tuple[str, str]:
        return full_name_str.split(" ")

    @classmethod
    def from_full_name(cls, name: str) -> Person:
        # calls Person(name_part[0], name_part[1])
        return cls(*Person.parse_full_name(name))

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        if not first_name:
            raise ValueError("first name must a string with some content")
        self.__first_name = first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        if not last_name:
            raise ValueError("last name must a string with some content")
        self.__last_name = last_name

    # instance method
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


p1 = Person("Bob", "Smith")
# calling the instance method full_name on the p1 object instance
print(p1.full_name())

p2 = Person("Alice", "Springs")
# calling the instance method full_name on the p2 object instance
print(p2.full_name())

# output the object id of the p1 full_name
# instance method function object
# instance method binds the self variable to the object instance
print(id(p1.full_name))

# output the object id of the p2 full_name
# instance method function object
# instance method binds the self variable to the object instance
print(id(p2.full_name))

p3 = Person.from_full_name("Tommy Jones")
print(p3.full_name())
print(p3.first_name)
print(p3.last_name)
