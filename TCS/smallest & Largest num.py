# 1
# def small_number(n):
#     return min(n)


# n = [2,5,1,4,7]
# print(small_number(n))

# 2
# def sort_arr(n):
#     n.sort()
#     a = n[-1]
#     return a

# n = [2,5,1,50,6]
# print(sort_arr(n))

# 3
def largest_num(arr,n):
    max = arr[0]
    for i in range(0,n):
        if(max < arr[i]):
            max = arr[i]
    return max
    
arr = [1,3,5,2,8]
n = 5
print(largest_num(arr,n))







# def largest_num(arr,n):
#     max = arr[0]
#     for i in range(0,n):
#         if(max < arr[i]):
#             max = arr[i]
#     return max

# arr = [3,2,5,7,8,42,46,5,111]
# n = 9
# print(largest_num(arr,n))