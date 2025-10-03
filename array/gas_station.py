class Solution(object):
    def canCompleteCircuit(self,gas,cost):
        n=len(gas)
        total=0
        leftover=0
        index=0
        for i in range(len(gas)):
            g = gas[i] - cost[i]
            total += g
            leftover += g
            if leftover < 0:
                index = i+1
                leftover = 0
        return index if total >= 0 and index < n else -1


obj = Solution()
gas=[2,3,4]
cost=[3,4,3]
print(obj.canCompleteCircuit(gas,cost))