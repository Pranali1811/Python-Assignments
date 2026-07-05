numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_even = len(list(filter(lambda x: x % 2 == 0, numbers)))
print(count_even)