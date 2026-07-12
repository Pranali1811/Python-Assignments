import multiprocessing
import os

def count_odd(n):
    # Logic: Odd count is (n + 1) // 2
    return {
        "pid": os.getpid(),
        "input": n,
        "odd": (n + 1) // 2
    }

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    
    with multiprocessing.Pool() as pool:
        results = pool.map(count_odd, data)
    
    for res in results:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Odd Number Count : {res['odd']}")
        print("-" * 30)

if __name__ == "__main__":
    main()