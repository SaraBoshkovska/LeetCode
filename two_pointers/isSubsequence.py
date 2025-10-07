class Solution(object):
    def isSubsequence(self,s,t):
        j = 0
        i = 0
        while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
        res = (i == len(s))
        return res

obj = Solution()
s = "axc" 
t = "ahbgdc"
print(obj.isSubsequence(s,t))