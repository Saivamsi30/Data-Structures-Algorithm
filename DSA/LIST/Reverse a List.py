# def reverse(l):
#     i = 0
#     j = len(l)-1
#     while i < j:
#         l[i],l[j] = l[j],l[i]
#         i += 1
#         j=j-1

# l = [3,4,5,6,7,8,9,0]
# reverse(l)
# print(l)

# def reverse(l):
#     i = 0
#     j = len(l)-1
#     while i < j:
#         l[i],l[j] = l[j],l[i]
#         i += 1
#         j -= 1

# user_input = input("Enter the values: ")

# l = list(map(int,user_input.split()))

# reverse(l)

# print(l)


# def reverse(l):
#     i = 0
#     j = len(l) -1
#     while i<j:
#         l[i],l[j] = l[j],l[i]
#         i += 1
#         j -= 1

# user_input = input("Enter the values: ")

# l = list(map(int,user_input.split()))

# reverse(l)

# print(l)


def reverse(n):
    i = 0
    j = len(n)-1
    while i < j :
        n[i],n[j] = n[j],n[i]
        i += 1
        j -= 1

user_input = input("Enter the values: ")

n = list(map(int,user_input.split()))

reverse(n)
print(n)