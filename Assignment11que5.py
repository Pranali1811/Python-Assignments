def check_palindrome(num):
    
    original_num = num
    reversed_num = 0
    
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
    
    if original_num == reversed_num:
        return "Palindrome"
    else:
        return "Not Palindrome"

user_input = 121
print(f"Input: {user_input}")
print(f"Output: {check_palindrome(user_input)}")