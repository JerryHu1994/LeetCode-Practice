class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:  return 0
        dp, currmax = [0]*len(nums), 0
        for i in range(len(nums)):
            if i+nums[i] > currmax:
                for j in range(currmax+1, i+nums[i]+1):
                    dp[j] = dp[i]+1
                    if j == len(nums)-1:    return dp[j]
                currmax = i+nums[i]
        return dp[-1]