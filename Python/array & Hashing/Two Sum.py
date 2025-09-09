#Brute Force method (Nested Loop) -------> O(n*n)

# class Solution:
#     def Twosum(self,nums:list[int],target:int)->list[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#             return[]
        
# nums = [1,2,4,5]
# target = 5
# obj = Solution()
# print(obj.Twosum(nums,target))

# Using Hashmap -------->O(n)

class Solution:
    def Twosum(self,nums:list[int],target:int)->list[int]:
        prevmap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n] = i
        return []
    
nums = [1,2,3,4]
target = 5
obj = Solution()
print(obj.Twosum(nums,target))

                             

