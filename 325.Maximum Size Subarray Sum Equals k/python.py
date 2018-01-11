class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums, currsum, maxlen = {0:0}, 0, 0
        for i,val in enumerate(nums):
            currsum += val
            if not currsum in sums: sums[currsum]=i+1
            if currsum-k in sums:   maxlen = max(maxlen, i+1-sums[currsum-k])
        return maxlen
                
        