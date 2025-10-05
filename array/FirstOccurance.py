class Solution(object):
    def strStr(self,haystack,needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack,needle))

