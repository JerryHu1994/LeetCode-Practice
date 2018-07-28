class Solution(object):
    
    def helper(self,nums):
        if len(nums)==0:    return 0
        if len(nums)==1:    return nums[0]
        if len(nums)==2:    return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0] # dp[i] means the largest ret we can get from nums[0] to nums[i]
        dp[1] = max(nums[0:2])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1]) # either include i or ignore i
        return dp[-1]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:    return 0
        if len(nums)==1:    return nums[0]
        if len(nums)==2:    return max(nums)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))