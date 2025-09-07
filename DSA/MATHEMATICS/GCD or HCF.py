def gcd(a,b):
    while a != b:
        if a>b:
            a = a - b
        else:
            b = b - a
    return a
    
a = 12
b = 15
print(gcd(a,b))

# a = [2,1,8,6,9,4]
# a.sort()
# print(a)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 12
b = 15
print(gcd(a, b))  # Output: 3

def gcd(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a