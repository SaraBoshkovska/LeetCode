class Solution(object):
    def lengthOfLastWord(self,s):
        word = s.split()[-1]
        return len(word)

obj = Solution()
s = "luffy is still joyboy"
print(obj.lengthOfLastWord(s))