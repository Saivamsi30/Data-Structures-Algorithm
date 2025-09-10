class Solution:
    def removeelement(self,nums:list[int],val:int)->int:
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index
    
nums = [3,2,2,3]
val = 3
obj = Solution()
print(obj.removeelement(nums,val))
