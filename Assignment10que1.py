def main():
    no = int(input("Enter a number: "))
    table = [str(no * i) for i in range(1, 11)]


    print(" ".join(table))

if __name__ == "__main__":
    main()