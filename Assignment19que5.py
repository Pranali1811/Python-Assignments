from functools import reduce

def ChkPrime(no):
    if no < 2: return False
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0: return False
    return True

arr = [2, 70, 11, 10, 17, 23, 31, 77]

filtered = list(filter(ChkPrime, arr))
mapped = list(map(lambda x: x * 2, filtered))
reduced = reduce(lambda x, y: x if x > y else y, mapped)

print("Filter:", filtered)
print("Map:", mapped)
print("Reduce:", reduced)