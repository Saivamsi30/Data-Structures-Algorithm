######### Left triangle with numbers

# n = 5
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end = " ")
#     p += 1
#     print()

########## Right triangle pattern(Numbers)

# n = 5
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end = " ")
#     for j in range(i,n):
#         print(p,end = " ")
#     p += 1    
#     print()

######### Hill pattern with numbers #########

# n = 5
# p = 1
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end = " ")
#     for j in range(i):
#         print(p,end = " ")
#     for j in range(i+1):
#         print(p,end = " ")
#     p += 1
#     print()

########### Reverse hill pattern with numbers ########

# n = 5
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end = " ")
#     for j in range(i,n-1):
#         print(p,end = " ")
#     for j in range(i,n):
#         print(p,end = " ")
#     p += 1
#     print()


#######################

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if (i%2 == 0):
#             print("1",end  = " ")
#         else:
#             print("2",end = " ")
#     print()

#####################

# n = 5

# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(p,end = " ")
#         p += 1
#     print()

################

# n = 5
# for i in range(n):
#     p = 1
#     for j in range(i,n):
#         print(" " , end =" ")
#     for j in range(i):
#         print(p,end = " ")
#         p += 1
#     for j in range(i+1):
#         print(p,end = " ")
#         p +=1
#     print()

#################

n = 5
p = 1
for i in range(n):
    for j in range(i+1):
        print(p,end = " ")
        p += 1
    print()