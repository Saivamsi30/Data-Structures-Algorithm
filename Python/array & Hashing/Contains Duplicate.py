class solution:
    def ContainsDuplicate(self,nums:list[int])->bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False
    
nums = [1,3,2,3]
obj = solution()
print(obj.ContainsDuplicate(nums))
