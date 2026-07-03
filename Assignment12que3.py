num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"\nAddition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")

if num2 != 0:
    division = num1 / num2
    print(f"Division: {num1} / {num2} = {division}")
else:
    print("Division: Cannot divide by zero.")