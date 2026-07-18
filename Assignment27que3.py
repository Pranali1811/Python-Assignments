class Numbers:

    
    def __init__(self, value):
        self.Value = int(value)

    
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

   
    def ChkPerfect(self):
        if self.Value <= 0:
            return False

        
        sum_divisors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_divisors += i

        return sum_divisors == self.Value

    def Factors(self):
        factors_list = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors_list.append(i)
        print(f"Factors of {self.Value}: {factors_list}")

    def SumFactors(self):
        total_sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total_sum += i
        return total_sum



print("--- Operating on Object 1 (Value: 6) ---")
obj1 = Numbers(6)
print(f"Is Prime?      : {obj1.ChkPrime()}")
print(f"Is Perfect?    : {obj1.ChkPerfect()}")
obj1.Factors()
print(f"Sum of Factors : {obj1.SumFactors()}")


print("\n--- Operating on Object 2 (Value: 11) ---")
obj2 = Numbers(11)
print(f"Is Prime?      : {obj2.ChkPrime()}")
print(f"Is Perfect?    : {obj2.ChkPerfect()}")
obj2.Factors()
print(f"Sum of Factors : {obj2.SumFactors()}")