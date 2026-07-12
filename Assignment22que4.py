import multiprocessing
import time

def calculate_sum_of_fifth_powers(n):
    """Calculates the sum of i^5 from 1 to N."""

    return sum(i**5 for i in range(1, n + 1))

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]
    
  
    start_time = time.perf_counter()
  
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sum_of_fifth_powers, numbers)
    

    end_time = time.perf_counter()
    
    for n, res in zip(numbers, results):
        print(f"N={n:7} | Sum of 5th powers: {res}")
        
    print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()