import json

people_dict = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Amy", "age": 20, "city": "London"},
    {"name": "Sri", "age": 40, "city": "Hyderabad"},
]


class Person:
    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city


people_obj = [
    Person("John", 30, "New York"),
    Person("Amy", 20, "London"),
    Person("Sri", 40, "Hyderabad"),
]


def main() -> None:
    # purpose of the with is to close the file after the block of
    # code is executed
    with open("data.json", "w") as file:
        json.dump([p.__dict__ for p in people_obj], file)

    with open("data.json", "r") as file:
        people2 = json.load(file)
        print([Person(p["name"], p["age"], p["city"]) for p in people2])


if __name__ == "__main__":
    main()
