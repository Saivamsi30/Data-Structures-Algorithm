# First Unique Character in a String
from collections import defaultdict
def uniqchar(s):
    count = defaultdict(int)

    for  c in s:
        count[c] += 1

    for i,c in  enumerate(s):
        if count[c] == 1:
            return i
    return -1
s = "loveleetcode"
print(uniqchar(s))

# String Rotation Check
class Solution:
    def areRotations(self,s1,s2):
        if len(s1) != len(s2):
            return False
        
        str = s1 + s1
        return s2 in str
    
s1 = "abcd"
s2 = "cdab"
obj = Solution()
print(obj.areRotations(s1,s2))