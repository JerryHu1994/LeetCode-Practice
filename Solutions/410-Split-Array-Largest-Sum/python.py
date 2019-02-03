class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[float("inf")]*(m+1)  for i in range(n+1)] # dp[i][j] stands for largest sum when spliting nums[1 .. i] into j pieces
        culsum = [0]*(n+1)
        for i in range(m+1):    dp[0][i] = 0
        for i in range(n):  culsum[i+1] = culsum[i]+nums[i]
        for i in range(1, n+1):
            for j in range(1, min(m+1, i+1)):
                # split with indexes before i 
                for k in range(j-1, i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], culsum[i]-culsum[k]))
        return dp[-1][-1]