import multiprocessing
import os

def calculate_even_sum(n):
    
    limit = n if n % 2 == 0 else n - 1

    even_sum = (limit // 2) * (limit // 2 + 1)
    
    return {
        "pid": os.getpid(),
        "input": n,
        "sum": even_sum
    }

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_even_sum, data)
    
    
    for res in results:
        print(f"Process ID : {res['pid']}")
        print(f"Input Number : {res['input']}")
        print(f"Sum of Even Numbers : {res['sum']}")
        print("-" * 30)

if __name__ == "__main__":
    main()