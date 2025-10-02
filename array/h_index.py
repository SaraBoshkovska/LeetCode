class Solution(object):

    def hIndex(self, citations):
        citations.sort(key=None, reverse=True)
        count = 1
        h = 0
        for i in range(1,len(citations)):
            if citations[i-1] >= count:
                h += 1
                count += 1
            elif citations[i-1] < count:
                return h
        return h

obj = Solution()
cit = [31,10,5,3,3]
print(obj.hIndex(cit))