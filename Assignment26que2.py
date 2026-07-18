class Circle:
    # Class variable
    PI = 3.14

    # Constructor initializing instance variables to 0.0
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0


    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))


    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius**2)

    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("\n--- Circle Details ---")
        print(f"Radius        : {self.Radius}")
        print(f"Area          : {self.Area}")
        print(f"Circumference : {self.Circumference}")



print("--- Object 1 ---")
c1 = Circle()
c1.Accept()
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()

print("\n--- Object 2 ---")
c2 = Circle()
c2.Accept()
c2.CalculateArea()
c2.CalculateCircumference()
c2.Display()