class Solution(object):
    
    def majorityElement(self, nums):
        dic = {}
        maxi=0
        m=nums[0]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        for key,value in dic.items():
            if value > maxi:
                maxi = value
                m = key

        return m

obj = Solution()
nums = [1,1,2,3,4,5,3,3]
print(obj.majorityElement(nums))