class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        dp = [[0]*(N+1) for i in range(L+1)] # dp[i][j]: # of ways to play total of i songs including j different songs
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1,L+1):
            for j in range(1,N+1):
                dp[i][j] += dp[i-1][j-1]*(N-j+1) # the song is the first time to be played
                dp[i][j] += dp[i-1][j]*max(j-K, 0) # the song is played once
                dp[i][j] = dp[i][j]%mod
        return dp[-1][-1]