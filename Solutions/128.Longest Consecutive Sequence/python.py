class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums)==1:    return 1
        nums = sorted(nums)
        ret = 0
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[right] - nums[right-1] == 1:
                right += 1
            ret = max(right - left, ret)
            left, right = right, right+1
        return ret
            