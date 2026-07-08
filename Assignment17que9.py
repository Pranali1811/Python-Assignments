def CountDigits(no):
    return len(str(no))

if __name__ == "__main__":
    val = int(input("Enter number: "))
    print("Number of digits:", CountDigits(val))