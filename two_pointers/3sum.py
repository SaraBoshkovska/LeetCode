class Solution(object):
    def threeSum(self,nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(0,n-3):
            p1=i+1
            p2=n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            while p1 < p2:
                r = nums[i] + nums[p1] + nums[p2]
                if r == 0:
                    res.append([nums[i],nums[p1],nums[p2]])
                    p1 += 1
                    p2 -= 1
                elif r < 0:
                    p1 += 1
                else:
                    p2 -= 1
        return res


obj = Solution()
nums = [-1,0,1,2,-1,-4]

print(obj.threeSum(nums))