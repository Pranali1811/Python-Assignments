def Frequency(arr, search_val):
    return arr.count(search_val)

if __name__ == "__main__":
    n = int(input("Number of elements: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    val = int(input("Element to search: "))
    print("Output:", Frequency(arr, val))