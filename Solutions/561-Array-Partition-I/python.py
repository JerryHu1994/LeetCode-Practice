class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        idx, ret = 0, 0
        while idx < len(nums):
            ret += nums[idx]
            idx += 2
        return ret 