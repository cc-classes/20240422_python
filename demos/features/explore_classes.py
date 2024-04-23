class Person:
    def __init__(
        self, first_name: str, last_name: str, age: int, city: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def full_name(self) -> str:
        return self.first_name + " " + self.last_name


# create an instance of the Person class
person = Person("John", "Doe", 30, "New York")
# call the full_name method on the instance (self=person)
print(person.full_name())  # John Doe

# instead of this
print(person.__dict__["first_name"])
# do this
print(person.first_name)

# instead of this
#full_name(person)
# do this
person.full_name()

# creates a second instance of the Person class
person2 = Person("Jane", "Doe", 30, "New York")
