class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 0 or len(A[0]) == 0:   return 0
        height, width = len(A), len(A[0])
        dp = [[float("inf")]*width for i in range(height)]
        for i in range(width):  dp[-1][i] = A[-1][i]
        for i in range(height-2, -1, -1):
            for j in range(width):
                dp[i][j] = min(dp[i][j], A[i][j]+dp[i+1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], A[i][j]+dp[i+1][j-1])
                if j < width-1:
                    dp[i][j] = min(dp[i][j], A[i][j]+dp[i+1][j+1])
        return min(dp[0])