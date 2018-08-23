class Solution(object):
    def dfs(self, nums, sums, pos, target):
        if pos == len(nums):    return True
        for i in xrange(4):
            if sums[i] + nums[pos] <= target:
                sums[i] += nums[pos]
                if self.dfs(nums, sums, pos+1, target): return True
                sums[i] -= nums[pos]
        return False

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:   return False
        sort = sorted(nums, reverse=True)
        s = sum(nums)
        if s%4 != 0:    return False
        target = s/4
        sums = [0]*4
        return self.dfs(sort, sums, 0, target)