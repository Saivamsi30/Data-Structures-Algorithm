# def fact(n):
#     res = 1
#     for i in range(2,n+1):
#         res = res*i
#     return res

# number = 5
# print(fact(number))

# def fact(n):
#     if n == 0:
#         return 1
    
#     return n * fact(n-1)


# number = 5
# print(fact(number))

#Recursive approach
# def fact(n):
#     if n == 0:
#         return 1
    
#     return n*fact(n-1)

# num = 3
# print(fact(num))

#Iterative approach

def fact(n):
    if n < 0:
        return False
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

n = 5
print(fact(n))

def fact(n):
    if n < 0:
        return False
    res = 1
    for i in range(1,n+1):
        res = res * 1
    return res

