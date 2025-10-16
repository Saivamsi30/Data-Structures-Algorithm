# Intersection of Two Arrays

def intersection(nums1,nums2):
    seen = set()
    nums2 = set(nums2)
    for i in nums1:
        if i in nums2:
            seen.add(i)
    return list(seen)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1,nums2))

# Majority Element (By Bayer Moore's Voting Algorithm)----Optimized Code

def majorityelement(nums):
    candidate = None
    count = 0
    for  i in nums:
        if count == 0:
            candidate = i
        if i == candidate:
            count += 1
        else:
            count -= 1
    return candidate

nums = [2,2,1,1,1,2,2]
print(majorityelement(nums))