class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[0]*n for a in range(m)]
        ret, dp[i][j] = 0, 1
        M = 1000000000 + 7
        for i in range(N):
            newdp = [[0]*n for k in range(m)]
            for a in range(m):
                for b in range(n):
                    if a == 0:  ret = (ret + dp[a][b])%M
                    if a == m-1:    ret = (ret + dp[a][b])%M
                    if b == 0:  ret = (ret + dp[a][b])%M
                    if b == n-1:    ret = (ret + dp[a][b])%M
                    if a > 0:   newdp[a][b] = (newdp[a][b] + dp[a-1][b])%M
                    if a < m-1: newdp[a][b] = (newdp[a][b] + dp[a+1][b])%M
                    if b > 0:   newdp[a][b] = (newdp[a][b] + dp[a][b-1])%M
                    if b < n-1: newdp[a][b] = (newdp[a][b] + dp[a][b+1])%M
            dp = newdp
            print ret
        return ret