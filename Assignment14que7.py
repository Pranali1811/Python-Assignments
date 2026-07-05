def main():
    is_divisible_by_5 = lambda x: x % 5 == 0
    value = int(input("Enter a number: "))
    result = is_divisible_by_5(value)
    print(result)

if __name__ == "__main__":
    main()