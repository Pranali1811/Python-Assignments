num = int(input("Enter a number: "))

temp = num
digit_sum = 0

while temp > 0:
    remainder = temp % 10    
    digit_sum += remainder   
    temp = temp // 10        

print(f"The sum of the digits of {num} is: {digit_sum}")