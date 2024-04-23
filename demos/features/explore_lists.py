from typing import Any

items: list[Any] = [1, "cool", lambda x: x + 1, {"name": "Bob"}, True]

nums: list[int] = [1, 2, 3, 4, 5]

letters: list[str] = ["a", "b", "c", "d", "e"]

# list of dictionaries whee each dictionary has keys
# that are strings, and the values can be any type
people: list[dict[str, Any]] = [
    {"name": "Bob", "age": 23},
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 27},

]

for person in people:
    print(person["name"], person["age"])

# add a new dictonary to the list
people.append({"name": "Cory", "age": 33})

for person in people:
    print(person["name"], person["age"])