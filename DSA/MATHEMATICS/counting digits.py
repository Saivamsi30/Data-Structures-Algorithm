# x = int(input('enter any num'))
# res = 0
# while x>0:
#     x = x//10
#     res = res+1

# print('count of the digits:',res)



# x = int(input())
# res = 0
# while x>0:
#     x = x//10
#     res += 1

# print("Count the digits: " , res)


# x = int(input())
# res = 0
# while x>0:
#     x = x//10
#     res +=1
# print("count digits: ", res)

# x = int(input())
# res = 0
# while x>0:
#     x = x//10
#     res +=1 
# print("Count Digits: ",res)



# num = int(input("Enter the number"))
# x = 0 
# temp = num
# while temp > 0:
#     digit = temp % 10
#     x = x*10 + digit
#     temp = temp//10

# if x == num:
#     print("It  is a Palindrome number")
# else:
#     print("It is not a Palindrome number")




# num = int(input("Enter the number"))
# res = 0
# temp = num
# while temp > 0:
#     temp = temp//10
#     res +=1
# print("Count digits: ",res)


# num = int(input())
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")


x = int(input())
res = 0
while x > 0:
    x = x//10
    res += 1
print("Count of digits: ",res)

