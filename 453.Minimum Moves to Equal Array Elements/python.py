class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val, s = float("inf"), 0
        for i in nums:
            s += i
            min_val = min(min_val, i)
        return s - len(nums)*min_val