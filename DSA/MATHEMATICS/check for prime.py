# def isprime(n):
#     if n == 1:
#         return False
    
#     for i in range(2,n):
#         if n % i == 0:
#             return False
        
#     return True

# a = 17
# print("Prime") if isprime(a) else print("not a prime") 

# # print(isprime(7))


# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# a = 7
# print("Prime") if is_prime(a) else print("not a prime")


# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
        
# a = 10
# print("Prime" if is_prime(a) else print("not a prime"))


# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# n = 11
# print(is_prime(n))    

def is_prime(n):
    if n == 0:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        return True

n = 4
print(is_prime(n))

#Q1
# input_1 = input()
# input_2 = input()
# rev = input_1[::-1]
# print(rev)
# if input_1 == input_2:
#     print(input_1 + ' and ' + input_2 +' are same')
# else:
#     print(input_1 + ' and ' + input_2 + ' are not same')


def is_prime(n):
    if n ==0:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
    
n = 9
print(is_prime(n))