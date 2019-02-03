class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:  return 1
        dp = [[0]*3 for i in range(N)]
        mod = 10**9+7
        # fill the base condition
        dp[0][0] = 1
        dp[1][0] = 2
        dp[0][1] = 0
        dp[0][2] = 0
        dp[1][1] = 1
        dp[1][2] = 1
        for i in range(2, N):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2])%mod
            dp[i][1] = (dp[i-1][2] + dp[i-2][0])%mod
            dp[i][2] = (dp[i-1][1] + dp[i-2][0])%mod
        return dp[-1][0]