class Solution:
    def Longestcommonprefix(self,strs:list[str])->str:
        if not strs:
            return ""
        
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
                
        return prefix
    
strs = ["flower","flow","flight"]
obj = Solution()
print(obj.Longestcommonprefix(strs))