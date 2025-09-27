# MAX ELEMENT IN AN ARRAY

# def maxvalue(arr):
#     if not arr:
#         return None
    
#     maxvalue = arr[0]
#     for num in arr:
#         if num > maxvalue:
#             maxvalue = num
        
#     return maxvalue

# arr = [1,2,9,4,6,8]
# print(maxvalue(arr))

# MIN ELEMENT IN AN ARRAY

# def minvalue(arr):
#     if not arr:
#         return None
#     minvalue = arr[0]
#     for num in arr:
#         if num < minvalue:
#             minvalue = num
#     return minvalue

# arr = [9,3,5,1,0,8]
# print(minvalue(arr))

# REVERSE AN ARRAY-------> O(1)

def revarr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr

arr = [1,4,6,8,4]
print(revarr(arr))

