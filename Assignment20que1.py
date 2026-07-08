import threading

def DisplayEven():
    print("Even numbers:")
    for i in range(2, 22, 2):
        print(i, end=" ")
    print("\n")

def DisplayOdd():
    print("Odd numbers:")
    for i in range(1, 20, 2):
        print(i, end=" ")
    print("\n")

if __name__ == "__main__":
    t1 = threading.Thread(target=DisplayEven, name="Even")
    t2 = threading.Thread(target=DisplayOdd, name="Odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()