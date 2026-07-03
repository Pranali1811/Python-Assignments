num = int(input("Enter a number: "))

if num <= 0:
    print("Not a Perfect Number")
else:
    divisor_sum = sum([i for i in range(1, num) if num % i == 0])
    
    if divisor_sum == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")