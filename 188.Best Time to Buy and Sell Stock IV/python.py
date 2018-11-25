class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1 or k < 1:    return 0
        if k > len(prices):
            ret = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]: ret += prices[i] - prices[i-1]
            return ret
        l = len(prices)
        local = [[0]*(k+1) for i in range(l)] # local[i][j] on ith day, maximum j trans happened, last on last day
        globa = [[0]*(k+1) for i in range(l)] # globa[i][j] on ith day, maximum j trans happened
        for i in range(1, l):
            diff = prices[i] - prices[i-1]
            for j in range(1, k+1):
                local[i][j] = max(globa[i-1][j-1] + max(diff, 0), local[i-1][j]+diff) # either globally j-1 trans, trans on ith day depending on the diff, or locally j trans, diff is carried over
                globa[i][j] = max(globa[i-1][j], local[i][j]) # either j trans on previous day, or j trans and last one on today
        return globa[-1][-1]