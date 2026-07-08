from functools import reduce
arr = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

filtered = list(filter(lambda x: x >= 70 and x <= 90, arr))
mapped = list(map(lambda x: x + 10, filtered))
reduced = reduce(lambda x, y: x * y, mapped)

print("Filter:", filtered)
print("Map:", mapped)
print("Reduce:", reduced)