class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:    return 0
        first = max(nums)
        idx = nums.index(first)
        nums.remove(first)
        second = max(nums)
        return idx if first >= 2*second else -1