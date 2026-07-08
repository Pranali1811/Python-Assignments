def DisplayNameLength(name):
    return len(name)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    length = DisplayNameLength(user_name)
    print(length)