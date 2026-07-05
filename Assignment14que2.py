def main():
    cube = lambda x: x ** 3
    value = int(input("Enter a number: "))
    result = cube(value)
    print(result)

if __name__ == "__main__":
    main()