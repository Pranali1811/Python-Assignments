def main():
    is_even = lambda x: x % 2 == 0
    value = int(input("Enter a number: "))
    result = is_even(value)
    print(result)

if __name__ == "__main__":
    main()