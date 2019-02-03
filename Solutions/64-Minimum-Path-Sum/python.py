class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height, width = len(grid), len(grid[0])
        dp = [[0]*width for i in range(height)]
        dp[0][0] = grid[0][0]
        for i in range(1, width):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, height):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, height):
            for j in range(1, width):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
            