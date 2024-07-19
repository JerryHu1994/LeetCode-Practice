class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # fill in bottom row
        height, width = len(grid), len(grid[0])
        dp = [[0]*width for i in range(height)]
        for i in range(width-2, -1, -1):
            dp[-1][i] = grid[-1][i+1] - grid[-1][i]
            if dp[-1][i+1] > 0:
                dp[-1][i] += dp[-1][i+1]
        for i in range(height-2, -1, -1):
            dp[i][-1] = grid[i+1][-1] - grid[i][-1]
            if dp[i+1][-1] > 0:
                dp[i][-1] += dp[i+1][-1]
        for i in range(height-2, -1, -1):
            for j in range(width-2, -1, -1):
                move_right = dp[i][j+1] + grid[i][j+1] - grid[i][j] if dp[i][j+1] > 0 else grid[i][j+1] - grid[i][j]
                move_down = dp[i+1][j] + grid[i+1][j] - grid[i][j] if dp[i+1][j] > 0 else grid[i+1][j] - grid[i][j]
                dp[i][j] = max(move_right, move_down)
        return max([max(row) for row in dp[:-1]] + [max(dp[-1][:-1])])