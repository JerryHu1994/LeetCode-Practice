class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        currmax = -float("inf")
        ret = 0
        for ind, val in enumerate(arr):
            currmax = max(currmax, val)
            if ind == currmax:  ret += 1
        return ret