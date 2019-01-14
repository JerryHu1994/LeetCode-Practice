class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0, 1]
        if N < 2:   return dp[N]
        for i in range(2, N+1):
            dp.append(dp[-2]+dp[-1])
        return dp[-1]