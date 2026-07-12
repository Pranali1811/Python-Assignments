import multiprocessing
import math
import os

def calculate_factorial(n):
   
    return {
        "pid": os.getpid(),
        "input": n,
        "factorial": math.factorial(n)
    }

def main():
    data = [10, 15, 20, 25]
    
   
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, data)
    
    for res in results:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Factorial : {res['factorial']}")
        print("-" * 30)

if __name__ == "__main__":
    main()