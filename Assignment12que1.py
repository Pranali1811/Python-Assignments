char = input("Input: ").strip()

if len(char) != 1 or not char.isalpha():
    print("Please enter exactly one alphabetic character.")
else:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Output: Vowel")
    else:
        print("Output: Consonant")