class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2 == 1:    return False
        s = sum(nums)
        dp = [False]*(s+1)
        dp[0] = True
        for i in nums:
            for j in range(s, -1, -1):
                if dp[j]:   dp[j+i] = True
        return dp[s/2]