# Contains Duplicate

def containsduplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

nums = [1,2,3,1]
print(containsduplicate(nums))

# Two Sum

def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

nums = [2,5,7,8]
target = 9
print(twosum(nums,target))