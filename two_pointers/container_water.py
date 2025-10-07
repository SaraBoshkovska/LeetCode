class Solution(object):
    def maxArea(self,height):
        i = 0
        j = len(height)-1
        best = 0
        while i < j:
            width = j - i 
            shorter = min(height[i],height[j]) 
            area = width * shorter 
            best = max(best, area) 
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return best

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))