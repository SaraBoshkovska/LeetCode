class Solution(object):
    def removeDuplicates(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] is not nums[i-1] and i-1 > 0:
                index += 1
                nums[index] = nums[i]
            else:
                continue
        del nums[index + 1:]
        return len(nums), nums

obj = Solution()

nums = [1,1,1,2,2,2,3,3]
print(obj.removeDuplicates(nums))