class Solution(object):

    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0: return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            dp = [costs[i][0]+min(dp[1], dp[2]), costs[i][1]+min(dp[0], dp[2]), costs[i][2]+min(dp[0], dp[1])]
        return min(dp)