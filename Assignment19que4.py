from functools import reduce

arr = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

filtered = list(filter(lambda x: x % 2 == 0, arr))
mapped = list(map(lambda x: x ** 2, filtered))
reduced = reduce(lambda x, y: x + y, mapped)

print("Filter:", filtered)
print("Map:", mapped)
print("Reduce:", reduced)