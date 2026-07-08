def PrintStars(no):
    for i in range(no):
        print("*", end="  ")

if __name__ == "__main__":
    val = int(input("Enter number of stars: "))
    PrintStars(val)