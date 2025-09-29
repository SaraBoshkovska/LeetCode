class Solution(object):
    '''
    def rotate(self,nums,k):
        nums.reverse()
        pom = 0
        for j in range(len(nums)):
            if j < k:
                for i in range(0,k-j-1):
                    pom = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = pom
            nums[k:] = reversed(nums[k:])
            
        return nums
       '''
    def rotate(self,nums,k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
            
        return nums
        

obj = Solution()
nums = [-1,-100,3,99]

k = 2
print(obj.rotate(nums,k))