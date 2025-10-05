class Solution(object):
    def reverseWord(self,s):
        s_arr = s.split()
        s_arr = s_arr[::-1]
        for i in range(len(s_arr)):
            if s_arr[i].isspace():
                s_arr.pop(i)
        back_to_s = " ".join(s_arr)
        return back_to_s

obj = Solution()
s = "luffy is  joyboy"

print(obj.reverseWord(s))