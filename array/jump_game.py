class Solution(object):
    '''
    def canJump(self,nums):
        
        n = 0
        i = 1
        while i < len(nums):
            n += nums[i] + i
            if n > len(nums):
                return False
            elif nums[i] == 0:
                return False
            else:
                i += n
     
        return True
    '''
    
    def canJump(self,nums) -> bool:
       k = 0
       for n in nums:
         if k < 0:
           return False
         elif n > k: 
           k = n
         k -= 1
       return True


obj = Solution()
nums = [2,3,1,1,2]
print(obj.canJump(nums))