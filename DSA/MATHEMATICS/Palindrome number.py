# def ispal(n):
#     rev = 0
#     temp = n
#     while temp != 0:
#         id = temp % 10
#         rev = rev * 10 + id
#         temp = temp//10
#     return rev == n

# n = 4554
# print(ispal(n))


#String Palindrome

# def ispalindrome(s):
#     temp = s
#     rev = temp[::-1]
#     print(rev)

#     if rev == temp:
#         return True
#     else:
#         return False

# s = "vamsi"
# print(ispalindrome(s))


def is_pal(s):
    if s==s[::-1]:
        return True
    else:
        return False

s = "vamsi"
if is_pal(s):
    print("Palindrome")
else:
    print("not a palindrome")
      

def is_pal(n):
    if s == s[::-1]:
        return True
    else:
        return False

s = "auaua"
if is_pal(s):
    print("Palindrome")

else:
    print("Not a Palindrome")   


#fibonacci series