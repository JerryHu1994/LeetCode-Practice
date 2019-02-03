class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        iterate = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        dp = [[1]*N for i in range(N)]
        for step in range(K):
            nextdp = [[0]*N for i in range(N)]
            for i in range(N):
                for j in range(N):
                    s = 0
                    for k in iterate:
                        jumpy, jumpx = i+k[0], j+k[1]
                        if jumpy < 0 or jumpy >= N or jumpx < 0 or jumpx >= N:  continue
                        s += float(dp[jumpy][jumpx])/8
                    nextdp[i][j] = s
            dp = nextdp
        return dp[r][c]