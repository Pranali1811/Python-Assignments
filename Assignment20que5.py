import threading

def PrintAscending():
    for i in range(1, 51):
        print(f"Thread1: {i}")

def PrintDescending():
    for i in range(50, 0, -1):
        print(f"Thread2: {i}")

if __name__ == "__main__":
    t1 = threading.Thread(target=PrintAscending, name="Thread1")
    t2 = threading.Thread(target=PrintDescending, name="Thread2")

    t1.start()
    t1.join()  
    t2.start()
    t2.join()