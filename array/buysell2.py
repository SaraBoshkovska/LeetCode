class Solution(object):
    def maxProfit(self,prices):
        profit=0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        return profit

obj = Solution()
prices = [7,1,5,3,6,4]
print(obj.maxProfit(prices))
        
