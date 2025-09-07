# # n = int(input("Enter the number"))

# # for i in range(1,n+1):
# #     if n%i == 0:
# #         flag = 0

# #         for j in range(2,i):
# #             if i%j == 0:
# #                 flag = 1
# #                 break

# #         if flag == 0:
# #             print(i,end=" ")



# def prime_fact(x):
#     prime_factors = []
#     divisor = 2

#     while divisor <= x:
#         if x%divisor == 0:
#             prime_factors.append(divisor)
#             x = x/divisor

#         else:
#             divisor += 1
#     return prime_factors

# print(prime_fact(100))

# def prime_fact(n):
#     prime_factors = []
#     divisor = 2

#     while divisor <= n:
#         if n % divisor == 0:
#             prime_factors.append(divisor)
#             n = n/divisor
#         else:
#             divisor +=1
#     return prime_factors

# print(prime_fact(50))






num = int(input("enter any number"))
n = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp = temp//10

if num == sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")















