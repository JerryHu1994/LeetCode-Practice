class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        goodidx = l-1
        for i in range(l-1, -1, -1):
            if i + nums[i] >= goodidx:
                goodidx = i
        return goodidx == 0