class Solution(object):
    def maxProfit(self,prices):
        mini = prices[0]
        maxi = 0
        for price in prices:
           profit = price - mini
           if profit > maxi:
               maxi = profit
           if price < mini:
               mini = price

        return maxi

obj = Solution()
prices = [7,1,5,3,6,4]
print(obj.maxProfit(prices))