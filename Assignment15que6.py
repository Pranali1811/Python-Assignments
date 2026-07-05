from functools import reduce
numbers = [12, 45, 2, 89, 34]
min_value = reduce(lambda x, y: x if x < y else y, numbers)

print(min_value)
