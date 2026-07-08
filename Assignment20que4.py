import threading
import os

def Small(s):
    count = sum(1 for char in s if char.islower())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {os.getpid()}")
    print(f"Lowercase Count: {count}")
    print("-" * 20)

def Capital(s):
    count = sum(1 for char in s if char.isupper())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {os.getpid()}")
    print(f"Uppercase Count: {count}")
    print("-" * 20)

def Digits(s):
    count = sum(1 for char in s if char.isdigit())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {os.getpid()}")
    print(f"Digits Count: {count}")
    print("-" * 20)

if __name__ == "__main__":
    data = input("Enter a string: ")
    t1 = threading.Thread(target=Small, args=(data,), name="Small")
    t2 = threading.Thread(target=Capital, args=(data,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(data,), name="Digits")
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()