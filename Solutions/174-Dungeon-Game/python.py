class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon) == 0 or len(dungeon[0]) == 0:   return 1
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*n for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j == n-1 and i == m-1:
                    dp[i][j] = 1 if dungeon[i][j] > 0 else -dungeon[i][j]+1
                    continue
                prev = None
                if j == n-1:
                    prev = dp[i+1][j]
                elif i == m-1:
                    prev = dp[i][j+1]
                else:
                    prev = min(dp[i+1][j], dp[i][j+1])
                curr = prev - dungeon[i][j]
                dp[i][j] = curr if curr > 0 else 1
        return dp[0][0]