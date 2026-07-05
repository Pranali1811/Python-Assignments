
numbers = [3, 5, 15, 20, 30, 45, 50, 60]
divisible_by_both = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

print(divisible_by_both)
