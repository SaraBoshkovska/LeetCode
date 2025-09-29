
class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for n in nums:
            if n is val:
                nums.pop(nums.index(n))
        return len(nums), nums

nums = [0,1,2,3,4,2,4]
val = 2
obj = Solution()
print(obj.removeElement(nums, val))


