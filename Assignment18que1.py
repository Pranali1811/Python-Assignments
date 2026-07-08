def SumList(arr):
    return sum(arr)

if __name__ == "__main__":
    n = int(input("Number of elements: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    print("Output:", SumList(arr))