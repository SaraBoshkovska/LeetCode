class Solution(object):
    def productExceptSelf(self,nums):
        answer = [1 for i in range(len(nums))]
        now = 0
        for i in range(len(nums)):
            now = nums[i]
            for j in range(len(nums)):
                if nums[j] != now:
                    answer[i] *= nums[j]
        return answer


obj = Solution()
nums = [-1,1,0,-3,3]
print(obj.productExceptSelf(nums))