class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for ind, val in enumerate(prices):
            if ind==0:  continue
            if (prices[ind-1] < val):   res += val - prices[ind-1]
        return res