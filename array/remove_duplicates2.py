class Solution(object):
    def removeDuplicates(self,nums):
        count = 0
        index = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                if count==2:
                    continue
                elif count==1:
                    index += 1
                    nums[index] = nums[i]
                    count += 1
            else:
                count=1
                index += 1
                nums[index] = nums[i]
        del nums[index+1:]
               
        return nums


obj = Solution()
nums = [1,1,1,2,2,2,3,3,4]
print(obj.removeDuplicates(nums))