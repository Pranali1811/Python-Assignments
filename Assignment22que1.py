import multiprocessing

def sum_of_squares(n):
    
    return (n * (n + 1) * (2 * n + 1)) // 6

def main():
    
    numbers = [1000000, 2000000, 3000000, 4000000]
    
 
    with multiprocessing.Pool() as pool:
       
        results = pool.map(sum_of_squares, numbers)
    
    print("Input List:", numbers)
    print("Sum of Squares:", results)

if __name__ == "__main__":
    main()