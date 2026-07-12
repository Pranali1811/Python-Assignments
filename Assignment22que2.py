import multiprocessing
import math
import os

def calculate_factorial(n):
   
    pid = os.getpid()
    result = math.factorial(n)
    return f"PID: {pid} | Input: {n} | Factorial: {result}"

def main():
    numbers = [10, 15, 20, 25]
    
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, numbers)
    
    for line in results:
        print(line)

if __name__ == "__main__":
    main()