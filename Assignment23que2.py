import multiprocessing
import os

def calculate_odd_sum(n):

    last_odd = n if n % 2 != 0 else n - 1
    
   
    k = (last_odd + 1) // 2
    
    
    odd_sum = k**2
    
    return {
        "pid": os.getpid(),
        "input": n,
        "sum": odd_sum
    }

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_odd_sum, data)
    
    for res in results:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Sum of Odd Numbers : {res['sum']}")
        print("-" * 30)

if __name__ == "__main__":
    main()