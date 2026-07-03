num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial deos not exist for negative number. ")

elif num ==0:
    print(1)

else:
    for i in range(1, num + 1):
        factorial *=1

        print(factorial)