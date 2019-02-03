class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        bestfund, besthold = 0, -prices[0] #best profit without a share, best profit with a share, on ith day
        for i in range(1,len(prices)):
            bestfund = max(bestfund, besthold+prices[i]-fee) #no hold -> keep no hold, has hold -> sell it
            besthold = max(bestfund-prices[i], besthold) #no hold->buy hold, has hold->keep hold
        return bestfund