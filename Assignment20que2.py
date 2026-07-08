import threading

def EvenFactor(no):
    sum_even = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            sum_even += i
    print(f"Sum of even factors: {sum_even}")

def OddFactor(no):
    sum_odd = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            sum_odd += i
    print(f"Sum of odd factors: {sum_odd}")

if __name__ == "__main__":
    number = int(input("Enter an integer: "))

    t1 = threading.Thread(target=EvenFactor, args=(number,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(number,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")