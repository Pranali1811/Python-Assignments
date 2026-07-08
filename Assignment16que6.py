def ChkNumber(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

if __name__ == "__main__":
    val = int(input("Enter a number: "))
    ChkNumber(val)