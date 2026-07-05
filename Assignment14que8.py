def main():
    add = lambda a, b: a + b
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    result = add(value1, value2)
    print(result)

if __name__ == "__main__":
    main()