from functools import reduce

numbers = [1, 2, 3, 4, 5]


total_sum = reduce(lambda x, y: x + y, numbers)

print(total_sum)
