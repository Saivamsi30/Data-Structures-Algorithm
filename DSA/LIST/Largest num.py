# def greater(l):
#     x = l[0]
#     for i in l:
#         if i > x:
#             x = i

#     return x

# l = [2,3,4,5,6,7,8,990]
# print(greater(l))

def large(l):
    n = len(l)
    for i in l:
        if i > n:
            n = i
    return n

user_input = input("Enter the values: ")
l = list(map(int,user_input.split()))
print(large(l))