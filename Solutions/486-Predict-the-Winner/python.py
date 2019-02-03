class Solution(object):

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        dp = [[0]*l for i in range(l)]
        for i in range(len(nums)-1, -1, -1):
            dp[i][i] = nums[i]
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0
                 