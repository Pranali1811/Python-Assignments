def MaxList(arr):
    return max(arr)

if __name__ == "__main__":
    n = int(input("Number of elements: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    print("Output:", MaxList(arr))