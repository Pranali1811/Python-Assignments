def AddFactors(no):
    sum_factors = 0
    for i in range(1, (no // 2) + 1):
        if no % i == 0:
            sum_factors += i
    return sum_factors

if __name__ == "__main__":
    val = int(input("Enter number: "))
    print("Addition of factors is:", AddFactors(val))