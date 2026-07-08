def Factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    return fact

if __name__ == "__main__":
    val = int(input("Enter number: "))
    print("Factorial is:", Factorial(val))