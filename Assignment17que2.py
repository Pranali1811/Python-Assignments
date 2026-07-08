def DisplayPattern(no):
    for i in range(no):
        print("* " * no)

if __name__ == "__main__":
    val = int(input("Enter number: "))
    DisplayPattern(val)