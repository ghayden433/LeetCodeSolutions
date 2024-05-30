class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        romanCon = (1, "I", 4, "IV", 5, "V", 9, "IX", 10, "X", 40, "XL", 50, "L", 90, "XC", 100, "C", 400, "CD", 500, "D", 900, "CM", 1000, "M")
        while (num > 0):
            for i in range (len(romanCon) - 2, -1, -2):
                if ((num - romanCon[i]) >= 0):
                    result = result + romanCon[i + 1]
                    num = num - romanCon[i]
                    break
        
        return result
        