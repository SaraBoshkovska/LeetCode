class Solution(object):
    def candy(self, ratings):
        candies = []
        candies = [1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(len(ratings) - 2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)

obj = Solution()
ratings = [1,0,2]
print(obj.candy(ratings))