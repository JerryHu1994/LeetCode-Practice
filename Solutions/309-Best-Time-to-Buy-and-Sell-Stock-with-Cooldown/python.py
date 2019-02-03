class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:    return 0
        buy = [0]*len(prices) # max profit when holding on day i
        sell = [0]*len(prices) # max profit when not holding on dayi
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            buy[i] = max(buy[i-1], sell[i-2]-prices[i] if i>=2 else -prices[i])
        return sell[-1]
        