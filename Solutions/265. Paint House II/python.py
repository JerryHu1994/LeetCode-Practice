class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0: return 0
        colors = len(costs[0])
        dp = costs[0]
        for i in range(1, len(costs)):
            nextdp = []
            for j in range(colors):
                nextdp.append(costs[i][j]+min(dp[:j]+dp[j+1:]))
            dp = nextdp
        return min(dp)
                