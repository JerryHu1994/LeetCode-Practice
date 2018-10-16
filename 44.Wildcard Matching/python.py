class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False]*(ls+1) for i in range(lp+1)]
        for i in range(ls+1):   dp[0][0] = True
        for i in range(1, lp+1):
            if p[i-1] == "*":
                dp[i][0] = True
            else:
                break
        for i in range(1,lp+1):
            for j in range(1, ls+1):
                pidx, sidx = i-1, j-1
                if p[pidx] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[pidx] == "*":
                    if True not in dp[i-1]: break
                    idx = dp[i-1].index(True)
                    for k in range(idx, ls+1):  dp[i][k] = True
                    break
                else:
                    if p[pidx] == s[sidx]:    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]        
        
        