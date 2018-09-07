class Solution(object):
    
    def helper(self, nums, currsums, target):
        if len(nums) == 0:   return True
        currmin = min(currsums)
        if target - currmin < nums[-1]:
            return False
        for i in range(len(currsums)):
            if currsums[i] + nums[-1] <= target: 
                currsums[i] += nums[-1]
                if self.helper(nums[:-1], currsums, target):
                    return True
                currsums[i] -= nums[-1]
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums)%k != 0:    return False
        subsum = sum(nums)/k
        nums = sorted(nums)
        return self.helper(nums, [0]*k, subsum)