class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not len(prices): return 0
        small, profit = prices[0],0
        for i in prices:
            if i-small > profit: profit=i-small
            if i<small: small=i
        return profit