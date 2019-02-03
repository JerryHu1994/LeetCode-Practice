class Solution(object):
    
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        height, width = len(s1), len(s2)
        dp = [[0]*(width+1) for i in range(height+1)]
        dp[height][width] = 0
        # on bottom
        for i in range(width-1, -1, -1):
            dp[height][i] = dp[height][i+1] + ord(s2[i])
        # on right
        for i in range(height-1, -1, -1):
            dp[i][width] = dp[i+1][width] + ord(s1[i])
        for i in range(height-1, -1, -1):
            for j in range(width-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(ord(s1[i])+dp[i+1][j], ord(s2[j])+dp[i][j+1])
        return dp[0][0]