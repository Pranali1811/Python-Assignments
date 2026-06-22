import sys
val = input("Enter value:")
print("Data type:",type(val))
print("memory address:",id(val))
print("size in bytes:",sys.getsizeof(val))