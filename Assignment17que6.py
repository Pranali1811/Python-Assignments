def Pattern(no):
    for i in range(no, 0, -1):
        print("* " * i)

if __name__ == "__main__":
    val = int(input("Enter number: "))
    Pattern(val)