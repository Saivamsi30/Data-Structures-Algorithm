class Solution:
    def removeduplicates(self,nums:list[int])->int:
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
    
nums = [0,0,1,2,2,3,4,4,4,5]
obj = Solution()
print(obj.removeduplicates(nums))