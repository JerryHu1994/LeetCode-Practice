class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:    return 0
        preprofits, currprofit, currmin = [], 0, prices[0]
        for i,v in enumerate(prices):
            currmin = min(currmin, v)
            currprofit = max(currprofit, v - currmin)
            preprofits.append(currprofit)
        currprofit, currmax = 0, prices[-1]
        ret = 0
        for i in range(len(prices)-1, -1, -1):
            currmax = max(currmax, prices[i])
            currprofit = max(currprofit, currmax - prices[i])
            ret = max(preprofits[i]+currprofit, ret)
        return ret