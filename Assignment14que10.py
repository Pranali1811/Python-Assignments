def main():
  
    get_max = lambda a, b, c: max(a, b, c)
    

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    n3 = float(input("Enter third number: "))
    
  
    print(f"The largest number is: {get_max(n1, n2, n3)}")

if __name__ == "__main__":
    main()