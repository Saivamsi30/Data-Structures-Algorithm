# Reverse a String

# def revstr(n):
#     left = 0
#     right = len(n) - 1
#     while left < right:
#         n[left],n[right] = n[right],n[left]
#         left += 1
#         right -= 1
#     return n

# n = ["h","e","l","l","o"]
# print(revstr(n))

# Valid Palindrome

# def ispal(s):
#     left = 0
#     right = len(s) -1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# s = "racecar"
# print(ispal(s))

# MORE OPTIMIZED

def ispal(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True

s = "A man, A plan, a canal: Panama"
print(ispal(s))