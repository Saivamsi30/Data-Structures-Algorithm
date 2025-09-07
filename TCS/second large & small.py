def second_largest(n):
    if len(n)<=1:
        return None
    large = n[0]
    slarge = None
    for i in n[1:]:
        if i < large:
            slarge = large
            large = i
        
        elif i != large:
            if slarge==None or slarge < i:
                slarge = i

    return slarge

n = [10,9]
print(second_largest(n))

#################################################

# def second_smallest(n):
#     if len(n) <= 1:
#         return None
    
#     small = n[0]
#     ssmall = None

#     for i in n[1:]:
#         if i < small:
#             ssmall = small
#             small = i

#         elif i != small:
#             if ssmall == None or ssmall > i:
#                 ssmall = i

#     return ssmall 

# n = [11,23,4,8,4,3,3,7]
# print(second_smallest(n))