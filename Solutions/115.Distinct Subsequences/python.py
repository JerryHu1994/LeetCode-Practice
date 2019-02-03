class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) == 0 or len(s) < len(t):  return 0
        dp = [[0]*len(s) for i in range(len(t))] # dp[i][j] stands for ways to generate distinct seqs for s[:j], t[:i]
        # populate first line
        count = 0
        for i in range(len(s)):
            if t[0] == s[i]:
                count += 1
            dp[0][i] = count
        for i in range(1,len(t)):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = dp[i-1][j-1] if t[i] == s[j] else 0
                    continue
                if t[i] == s[j]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
        