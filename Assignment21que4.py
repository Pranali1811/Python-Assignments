import threading
import math

results = {}

def CalculateSum(arr):
    results['sum'] = sum(arr)

def CalculateProduct(arr):
    results['prod'] = math.prod(arr)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    t1 = threading.Thread(target=CalculateSum, args=(arr,))
    t2 = threading.Thread(target=CalculateProduct, args=(arr,))
    
    t1.start(); t2.start()
    t1.join(); t2.join()
    
    print(f"Sum: {results['sum']}, Product: {results['prod']}")