def AddDigits(no):
    sum_digits = 0
    while no > 0:
        sum_digits += no % 10
        no //= 10
    return sum_digits

if __name__ == "__main__":
    val = int(input("Enter number: "))
    print("Addition of digits:", AddDigits(val))