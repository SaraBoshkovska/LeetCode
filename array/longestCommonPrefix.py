class Solution(object):
    def longestCommonPrefix(self,strs):
        s = strs[0]
        for st in range(1,len(strs)):
            while s not in strs[st]:
                s = s[:-1]
                if s == "":
                    return s
        return s
        

obj = Solution()
strs = ["flower","flow","flight"]
print(obj.longestCommonPrefix(strs))
s = "sa"
