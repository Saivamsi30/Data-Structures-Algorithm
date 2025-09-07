########### Right sided triangle ##########
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end = " ")
#     for j in range(i+1):
#         print("*",end = " ")
#     print()


# 2 #
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end = " ")
#     for j in range(i,n):
#         print("*",end = " ")
#     print()

########## hill pattern ########

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end = " ")
#     for j in range(i):
#         print("*",end = " ")
#     for j in range(i+1):
#         print("*",end = " ")

#     print()


############# Reverse Hill pattern ##########

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" " , end = " ")
#     for j in range(i,n-1):
#         print("*",end = " ")
#     for j in range(i,n):
#         print("*",end= " ")
#     print()


########### Diamond pattern #########

# n = 5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end = " ")
#     for j in range(i):
#         print("*",end = " ")
#     for j in range(i+1):
#         print("*",end = " ")

#     print()
     
# for i in range(n):
#     for j in range(i+1):
#         print(" " , end = " ")
#     for j in range(i,n-1):
#         print("*",end = " ")
#     for j in range(i,n):
#         print("*",end= " ")
#     print()

########### Double hill ############

n  =5
for i in range(n):
    for j in range(i,n):
        print(" ",end = " ")
    for i in range(i+1):
        print("*",end = " ")
    for j in range(i):
        print("*",end = " ")
    for j in range(1,n):
        print(" ",end = " ")
    for j in range(1,n):
        print(" ",end = " ")

    print()

