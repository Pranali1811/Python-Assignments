import threading

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def PrimeThread(numbers):
    primes = [n for n in numbers if is_prime(n)]
    print(f"Prime numbers: {primes}")

def NonPrimeThread(numbers):
    non_primes = [n for n in numbers if not is_prime(n)]
    print(f"Non-prime numbers: {non_primes}")

if __name__ == "__main__":
    data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    t1 = threading.Thread(target=PrimeThread, args=(data,), name="Prime")
    t2 = threading.Thread(target=NonPrimeThread, args=(data,), name="NonPrime")
    t1.start(); t2.start(); t1.join(); t2.join()
