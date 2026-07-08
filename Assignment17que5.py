def ChkPrime(no):
    if no < 2:
        return False
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            return False
    return True

if __name__ == "__main__":
    val = int(input("Enter number: "))
    if ChkPrime(val):
        print("It is Prime Number")
    else:
        print("It is not a Prime Number")