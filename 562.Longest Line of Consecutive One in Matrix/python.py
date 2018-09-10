class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M)==0 or len(M[0])==0:   return 0
        dp, height, width = [], len(M), len(M[0])
        for i in range(height):
            dp.append([])
            for j in range(width):
                dp[i].append([1,1,1,1] if M[i][j] == 1 else [0,0,0,0])
        ret = 0
        for i in range(height):
            for j in range(width):
                if j > 0 and dp[i][j][0] == 1:  dp[i][j][0] = dp[i][j-1][0] + 1
                if j > 0 and i > 0 and dp[i][j][1] == 1:    dp[i][j][1] = dp[i-1][j-1][1] + 1
                if i > 0 and dp[i][j][2] == 1:  dp[i][j][2] = dp[i-1][j][2] + 1
                if j < width-1 and i > 0 and dp[i][j][3] == 1:    dp[i][j][3] = dp[i-1][j+1][3] + 1
                ret = max(max(dp[i][j]), ret)
        return ret