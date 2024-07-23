class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxFuture = [0] * len(prices)
        most = 0
        maxProfit = 0
        for i in range(len(prices)):
            if prices[len(prices) - i - 1] > most:
                most = prices[len(prices) - i - 1] 
            maxFuture[len(maxFuture) - i - 1] = most
        
        for i in range(len(prices)):
            if maxFuture[i] - prices[i] > maxProfit:
                maxProfit = maxFuture[i] - prices[i]

        return maxProfit

        