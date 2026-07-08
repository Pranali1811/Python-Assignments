import threading

def FindMax(arr):
    print(f"Maximum: {max(arr)}")

def FindMin(arr):
    print(f"Minimum: {min(arr)}")

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    t1 = threading.Thread(target=FindMax, args=(arr,))
    t2 = threading.Thread(target=FindMin, args=(arr,))
    t1.start(); t2.start(); t1.join(); t2.join()