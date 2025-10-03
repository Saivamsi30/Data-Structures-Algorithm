def singlenum(nums):
    res = 0
    for i in nums:
        res = i ^ res
    return res

nums = [1,2,2,4,1]
print(singlenum(nums))