class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        currMin = 11000
        maxProfit = 0
        for price in prices:
            if price < currMin:
                currMin = price
            if price - currMin > maxProfit:
                maxProfit = price - currMin

        return maxProfit

        