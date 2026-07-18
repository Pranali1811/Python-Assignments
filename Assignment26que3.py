class Arithmetic:

   
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

   
    def Accept(self):
        self.Value1 = int(input("Enter first value (Value1): "))
        self.Value2 = int(input("Enter second value (Value2): "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    
    def Multiplication(self):
        return self.Value1 * self.Value2

   
    def Division(self):
        if self.Value2 == 0:
            return "Error: Division by zero is not allowed."
        return self.Value1 / self.Value2



print("--- Operating on Object 1 ---")
obj1 = Arithmetic()
obj1.Accept()
print(f"Addition       : {obj1.Addition()}")
print(f"Subtraction    : {obj1.Subtraction()}")
print(f"Multiplication : {obj1.Multiplication()}")
print(f"Division       : {obj1.Division()}")

print("\n--- Operating on Object 2 ---")
obj2 = Arithmetic()
obj2.Accept()
print(f"Addition       : {obj2.Addition()}")
print(f"Subtraction    : {obj2.Subtraction()}")
print(f"Multiplication : {obj2.Multiplication()}")
print(f"Division       : {obj2.Division()}")