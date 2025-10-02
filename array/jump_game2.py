class Solution(object):
    """
    BUGGING
    def jump(self,nums):
        sum = 0
        
        k = 0
        pom = []
        last = len(nums) 
        for i,n in enumerate(nums):
            sum = n
            k += 1
            for j in range(i+1,len(nums)):
                sum += nums[j]
                k += 1
                if sum == last:
                    pom.append(k)
                    break
        mini = pom[0]
        for p in pom:
            if mini > p:
                mini = p
        return mini
    """
    def jump(self,nums):
        last = 0
        farthest = 0
        j = 0
        for i,n in enumerate(nums):
            farthest = max(farthest, i+n)
            if i == last and i != len(nums) - 1:
                j += 1
                last = farthest
            
        return j
      

obj = Solution()
nums = [2,2,0,1,4]


print(obj.jump(nums))