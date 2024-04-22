from typing import Any

items: list[Any] = [1, "cool", lambda x: x + 1, {"name": "Bob"}, True]

nums: list[int] = [1, 2, 3, 4, 5]

letters: list[str] = ["a", "b", "c", "d", "e"]

# list of dictionaries where each dictionary has keys
# that are strings, and the values can be any type
people: list[dict[str, Any]] = [
    {"name": "Bob", "age": 23, "hair_color": "brown"},
    {"name": "Alice", "age": 25, "hair_color": "brown"},
    {"name": "Charlie", "age": 27, "hair_color": "brown"},
    {"name": "Diana", "age": 31, "hair_color": "brown"},
]

for person in people:
    print(person["name"], person["age"])

# add a new dictionary to the list
people.append({"name": "David", "age": 29, "hair_color": "brown"})

for person in people:
    print(person["name"], person["age"])
