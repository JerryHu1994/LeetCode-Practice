class Solution(object):

    
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0]*len(piles) for i in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for i in range(len(piles)-1, -1, -1):
            for j in range(i+1, len(piles), 1):
                    dp[i][j] = max(dp[i+1][j], sum(piles[i+1:j+1])-dp[i+1][j]+piles[i], dp[i][j-1], sum(piles[i:j])-dp[i][j-1]+piles[j])
        return dp[0][-1] > sum(piles)-dp[0][-1]