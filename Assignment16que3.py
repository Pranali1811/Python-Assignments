def Add(no1, no2):
    return no1 + no2

if __name__ == "__main__":
    
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    result = Add(val1, val2)
    print("Addition is:", result)