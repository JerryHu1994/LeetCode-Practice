class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:  return 0
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(dp)==1:  return max(dp)
        dp[1] = nums[1]
        if len(dp)==2:  return max(dp)
        dp[2] = nums[0] + nums[2]
        if len(dp)==3:  return max(dp)
        for i in range(3, len(dp)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
        return max(dp)
            