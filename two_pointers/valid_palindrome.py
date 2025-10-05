class Solution(object):
    def isPalindrome(self,s):
        st = ""
        for i in s:
            if i.isalnum():
                st += i.lower()
        if st == st[::-1]:
            return True
        else:
            return False


obj = Solution()
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))