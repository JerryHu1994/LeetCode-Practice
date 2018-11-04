class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0]*(N+1)
        for i in range(1, N+1):
            dp[i] = i
            for j in range(max(i-2-5,1), i-2):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        return dp[-1]