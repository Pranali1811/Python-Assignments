import threading

counter = 0
counter_lock = threading.Lock()

def IncrementCounter(amount):
    global counter
    for _ in range(amount):
        with counter_lock:
            counter += 1

if __name__ == "__main__":
    threads = []
    for _ in range(5):
        t = threading.Thread(target=IncrementCounter, args=(1000,))
        threads.append(t)
        t.start()
    
    for t in threads: t.join()
    print(f"Final counter value: {counter}")