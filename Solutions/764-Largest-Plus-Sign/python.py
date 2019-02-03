
class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        banset = set()
        ret = 0
        for i in mines:
            banset.add(tuple(i))
        height, width = N, N
        dp = [[0]*width for i in range(height)]
        # move horizontally
        for i in range(height):
            count = 0
            for j in range(width):
                count = 0 if (i, j) in banset else count+1
                dp[i][j] = count
            count = 0
            for j in range(width-1, -1, -1):
                count = 0 if (i, j) in banset else count+1
                dp[i][j] = min(dp[i][j], count)
        # move vertically
        for i in range(width):
            count = 0
            for j in range(height):
                count = 0 if (j,i) in banset else count+1
                dp[j][i] = min(dp[j][i], count)
            count = 0
            for j in range(height-1, -1, -1):
                count = 0 if (j, i) in banset else count+1
                dp[j][i] = min(dp[j][i], count)
                ret = max(ret, dp[j][i])
        return ret