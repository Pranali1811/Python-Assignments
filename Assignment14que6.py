def main():
    is_odd = lambda x: x % 2 != 0
    value = int(input("Enter a number: "))
    result = is_odd(value)
    print(result)

if __name__ == "__main__":
    main()