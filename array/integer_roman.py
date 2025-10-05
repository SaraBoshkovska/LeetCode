class Solution(object):

    def converting(self):
        """
        Python 3.7+ (it does not work in LeetCode Terminal)
        pairs = {1000:"M",
                900:"CM", 
                500:"D",
                400:"CD",
                100:"C",
                90:"XC",
                50:"L",
                40:"XL",
                10:"X",
                9:"IX",
                5:"V",
                4:"IV",
                1:"I"}
        """
        pairs = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"),
                (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),
                (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]
        return pairs

    def intToRoman(self, num):
        pom = []
        """
        for key,value in self.converting().items():
        """
        for key,value in self.converting():
                while num >= key:
                    pom.append(value)
                    num -= key
        pom_str = "".join(pom)
        return pom_str


obj = Solution()
num = 3749
print(obj.intToRoman(num))