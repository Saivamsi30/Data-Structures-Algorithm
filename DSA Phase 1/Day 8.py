# Count vowels and consonants

def checkString(s):
    v = "aeiou"
    count_v = 0
    count_c = 0
    for i in range(len(s)):
        if s[i].lower() in v:
            count_v += 1
        elif s[i].isalnum():
            count_c += 1
    
    if count_v > count_c:
        return "YES"
    elif count_v < count_c:
        return "NO"
    else:
        return "SAME"
    

s = "aaappp"
print(checkString(s))

# Valid Anagram

class Solution:
    def validanagram(self,s,t):
        if len(s) != len(t):
            return False
        
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.validanagram(s,t))