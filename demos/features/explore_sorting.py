from random import randint

# basic sorting of values with inherent sort order
# nums = [randint(0, 10) for _ in range(10)]
# print(nums)

# # sort the list in place (mutating the origina list)
# # nums.sort()

# # sort a copy of the original, leaving the original unchanged
# print(sorted(nums))
# print(nums)


class Food:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __str__(self):
        return f"name: {self.name}, country: {self.country}"


foods = [
    Food("kubben", "Iraq"),
    Food("steak", "US"),
    Food("crabcakes", "Maryland"),
    Food("sushi", "Japan"),
    Food("toad in the hole", "England"),
    Food("peking duck", "China"),
]

print(list(reversed([str(f) for f in sorted(foods, key=lambda x: x.country)])))

# foods.sort(key=lambda x: x.country)

# print([str(f) for f in foods])
