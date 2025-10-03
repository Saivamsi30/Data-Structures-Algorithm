# Remove Duplicates(Sorted Array)

def removeduplicates(nums):
    l = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[l] = nums[i]
            l += 1
    return l

nums = [1,2,2,4,5,6,6]
print(removeduplicates(nums))

# Merge Sorted Array

def merge(nums1,m,nums2,n):
    i = m-1
    j = n - 1
    k = m + n -1
    while j >=0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [1,2,4]
n = 3
merge(nums1,m,nums2,n)
print(nums1)

