class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0:0} # dp[d] is the max pair of sum with pair difference d
        for x in rods:
            curr = {i: dp[i] for i in dp}
            for d in curr:
                dp[d+x] = max(dp.get(x+d, 0), curr[d])
                dp[abs(d-x)] = max(dp.get(abs(d-x), 0), curr[d]+min(x, d))
        return dp[0]