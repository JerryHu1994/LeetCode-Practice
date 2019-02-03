class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)
        ret = float("inf")
        total_sum = sum(sort)
        left_sum = 0
        for ind, val in enumerate(sort):
            left_sum += val
            left_count = ind+1
            curr_bar = val
            curr_val = left_count*curr_bar - left_sum + total_sum - left_sum - (len(nums)-left_count)*curr_bar
            print curr_val
            ret = min(curr_val, ret)
        return ret