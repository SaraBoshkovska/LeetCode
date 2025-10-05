class Solution(object):
    def converting(self,num):
        """
        match num:
            case "M":
                return 1000
            case "D":
                return 500
            case "C":
                return 100
            case "L":
                return 50
            case "X":
                return 10
            case "V":
                return 5
            case "I":
                return 1
        """
        table = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        return table[num]
            
    def romanToInt(self, s):
        roman = list(s)
        sum_all = 0
        for r in range(len(roman)-1):
            num = self.converting(roman[r])
            num2= self.converting(roman[r+1])
            if num < num2:
                sum_all += -num
            else:
                sum_all += num
        sum_all += self.converting(roman[-1])

        return sum_all
            
obj = Solution()
s = "XIV"
print(obj.romanToInt(s))