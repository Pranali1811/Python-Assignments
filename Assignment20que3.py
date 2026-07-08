import threading

def EvenList(numbers):
    sum_even = sum(n for n in numbers if n % 2 == 0)
    print(f"Sum of even elements: {sum_even}")

def OddList(numbers):
    sum_odd = sum(n for n in numbers if n % 2 != 0)
    print(f"Sum of odd elements: {sum_odd}")

if __name__ == "__main__":
    data = [13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]
    t1 = threading.Thread(target=EvenList, args=(data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(data,), name="OddList")
    t1.start()
    t2.start()
    t1.join()
    t2.join()