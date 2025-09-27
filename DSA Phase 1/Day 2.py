# SECOND LARGEST ELEMENT

# def second_largest(arr):
#     largest = -1
#     second_largest = -1
#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num < largest and num > second_largest:
#             second_largest = num
#     return second_largest

# arr = [10,5,10]
# print(second_largest(arr))

# MOVE ZEROES (Using Two Pointers)

def movezeroes(nums):
    pos = 0
    for i in nums:
        if i != 0:
            nums[pos] = i
            pos += 1

    while pos < len(nums):
        nums[pos] = 0
        pos += 1

nums = [0,1,0,3,12]
movezeroes(nums)
print(nums)

