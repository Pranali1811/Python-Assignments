num_str = input("Input: ")

if num_str.startswith('-'):
    num_str = num_str[1:]

print(f"Output: {len(num_str)}")