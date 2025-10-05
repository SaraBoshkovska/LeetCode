class Solution(object):
    def zigzag(self, s, numRows):

        result = ""
        dic = {}
        k = 0
        n = len(s)
        
        while k < n:
            for i in range(numRows):
                if k>=n:
                    break
                dic[i] = dic.get(i, "") + s[k]
                k += 1
            for i in range(numRows-2,0,-1):
                if k >= n:
                    break
                dic[i] = dic.get(i, "") + s[k]
                k += 1
        for i in range(numRows):
            result += "".join(dic.get(i, ""))
        return result

obj = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(obj.zigzag(s,numRows))
        
