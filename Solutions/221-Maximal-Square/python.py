class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        height, width = len(matrix), len(matrix[0])
        ret = 0
        dp = [[0]*width for i in range(height)]
        for i in range(width):
            dp[0][i] = 1 if matrix[0][i] == "1" else 0
            ret = max(ret, dp[0][i])
        for i in range(height):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            ret = max(ret, dp[i][0])
        for i in range(1, height):
            for j in range(1,width):
                if matrix[i][j] == "0":   continue
                dp[i][j] = min([dp[i-1][j-1], dp[i][j-1], dp[i-1][j]]) + 1
                ret = max(ret, dp[i][j]**2)
        return ret
        