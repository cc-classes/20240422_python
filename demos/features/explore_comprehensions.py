# nums = list(range(10))
# # double_even_nums = []

# # for num in nums:
# #     if num % 2 == 0:
# #         double_even_nums.append(num * 2)

# # list comprehension - iterate and evaluate a conditional
# double_even_nums = [num * 2 for num in nums if num % 2 == 0]

# print(nums)
# print(double_even_nums)

# dictionary comprehension

# currencies = [("bitcoin", "BTC"), ("litecoin", "LTC"), ("ethereum", "ETH")]

# currencies_dict = {name: symbol for name, symbol in currencies}

# print(currencies_dict)

# set comprehension

# nums = [1, 2, 1, 2, 2, 2, 4, 5, 5]
# print(nums)

# nums_set = {num for num in nums}
# print(nums_set)

# generator comprehension

nums = list(range(10))

double_nums = (num * 2 for num in nums)

print(double_nums)

for double_num in double_nums:
    print(double_num)
