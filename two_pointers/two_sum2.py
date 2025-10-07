class Solution(object):
    def twoSum(self, numbers, target):
        """
        O(n²)
        for i in range(len(numbers)):
            for j in range(len(numbers)-1,i,-1):
                if numbers[i] + numbers[j] < target:
                    break
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1] 
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            res = numbers[i] + numbers[j]
            if res == target:
                return [i+1,j+1]
            if res < target:
                i += 1
            else:
                j -= 1
    
                            

obj = Solution()
numbers = [2,3,4]
target = 6
print(obj.twoSum(numbers, target))