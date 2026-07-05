minimum = lambda a, b: a if a < b else b
def main():
   
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = minimum(value1, value2)
    print(result)

if __name__ == "__main__":
    main()