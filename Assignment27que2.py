class BankAccount:
    # Class variable
    ROI = 10.5

    
    def __init__(self, name, amount):
       
        self.Name = name
        self.Amount = float(amount)

  
    def Display(self):
        print(f"\nAccount Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")

  
    def Deposit(self):
        dep_amount = float(input("Enter amount to deposit: "))
        self.Amount += dep_amount
        print(f"Successfully deposited {dep_amount}. New Balance: {self.Amount}")

    
    def Withdraw(self):
        with_amount = float(input("Enter amount to withdraw: "))
        if with_amount > self.Amount:
            print("Insufficient balance! Transaction denied.")
        else:
            self.Amount -= with_amount
            print(
                f"Successfully withdrew {with_amount}. Remaining Balance: {self.Amount}"
            )

   
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest




print("--- Creating Account 1 ---")
ac1 = BankAccount("Aditya", 5000)
ac1.Display()

ac1.Deposit()
ac1.Withdraw()
interest_earned1 = ac1.CalculateInterest()
print(f"Calculated Interest (at {BankAccount.ROI}%): {interest_earned1}")

print("\n--- Creating Account 2 ---")
ac2 = BankAccount("Neha", 1500)
ac2.Display()


ac2.Withdraw()
interest_earned2 = ac2.CalculateInterest()
print(f"Calculated Interest (at {BankAccount.ROI}%): {interest_earned2}")