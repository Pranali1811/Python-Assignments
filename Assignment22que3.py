import multiprocessing

def count_primes(n):
    if n < 2:
        return f"Input: {n} | Prime Count: 0"
    
    # Sieve of Eratosthenes
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    
    prime_count = sum(sieve)
    return f"Input: {n} | Prime Count: {prime_count}"

def main():
    numbers = [10000, 20000, 30000, 40000]
    
    with multiprocessing.Pool() as pool:
        results = pool.map(count_primes, numbers)
    
    for line in results:
        print(line)

if __name__ == "__main__":
    main()