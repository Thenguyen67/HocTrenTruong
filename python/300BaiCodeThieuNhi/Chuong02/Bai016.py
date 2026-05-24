def isPalindrome(str0):
    str0 = ''.join(i.lower() for i in str0 if i.isalnum())
    return str0 == str0[::-1]

print(isPalindrome(input()))

print(isPalindrome(input()))