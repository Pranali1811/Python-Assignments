import multiprocessing
import os

def count_even(n):
    
    return {
        "pid": os.getpid(),
        "input": n,
        "even": n // 2
    }

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    
    with multiprocessing.Pool() as pool:
        results = pool.map(count_even, data)
    
    for res in results:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Even Number Count : {res['even']}")
        print("-" * 30)

if __name__ == "__main__":
    main()