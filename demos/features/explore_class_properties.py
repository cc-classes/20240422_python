class Person:
    def __init__(self, fn: str, ln: str) -> None:
        self.__first_name = fn
        self.__last_name = ln

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


person = Person("Bob", "Smith")
person.first_name = None
person.last_name = "Smith"
