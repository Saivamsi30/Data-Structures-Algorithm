# def sorted(l):
#     i = 1
#     while i < len(l):
#         if l[i] < l[i-1]:
#             return False
#         i = i+1
#     return True
        
        
# l = [10,20,15,40,50]
# if sorted(l):
#     print("Yes")

# else:
#     print("No")


def sorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i += 1
    return True

l = [10,20,30,40,50]
if sorted(l):
    print("Yes")
else:
    print("No")