#1 Contains Duplicate (Using Hashset)

# class Solution:
#     def containsduplicate(self,nums:list[int])->bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

# nums = [1,2,3,4]
# obj = Solution()
# print(obj.containsduplicate(nums))

#2 Valid Anagram (Using hashmap)

# class Solution:
#     def isanagram(self,s:str,t:str)-> bool:
#         if len(s) != len(t):
#             return False
        
#         countS, countT = {},{}

#         for i in range(len(s)):
#              countS[s[i]] = 1+countS.get(s[i],0)
#              countT[t[i]] = 1+countT.get(t[i],0)

#         for c in countS:
#             if countS[c] != countT.get(c,0):
#                 return False
#         return True
    
# s = "anagram"
# t = "nagaram"
# obj = Solution()
# print(obj.isanagram(s,t))

#3 Two Sum 
# Using Brute force method /two pointers o(n*n)

# class Solution:
#     def twosum(self,nums:list[int],target:int)->list[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#             return []
        
# nums = [1,3,5,7]
# target = 6
# obj = Solution()
# print(obj.twosum(nums,target))

# Using Hashmap----o(n)

# class Solution:
#     def twosum(self,nums:list[int],target:int)->list[int]:
#         prevmap = {}

#         for i,n in enumerate(nums):
#             diff = target - n
#             if diff in prevmap:
#                 return [prevmap[diff],i]
#             prevmap[n] = i

#         return 
    
# nums = [1,3,5,7]
# target = 6
# obj = Solution()
# print(obj.twosum(nums,target))


#4 reverse an array (using two pointers)


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

def minvalue(arr):
    if not arr:
        return None
    minvalue = arr[0]
    for num in arr:
        if num < minvalue:
            minvalue = num
    return minvalue

arr = [9,3,5,1,0,8]
print(minvalue(arr))




    

