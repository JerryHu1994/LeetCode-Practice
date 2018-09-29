class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        pairs = []
        for ind,val in enumerate(arr):
            pairs.append([val, ind])
        sorted_pairs = sorted(pairs, key = lambda x:[x[0], x[1]])
        for ind, sp in enumerate(sorted_pairs):
            arr[sp[1]] = ind
        currmax = -float("inf")
        ret = 0
        for ind, val in enumerate(arr):
            currmax = max(currmax, val)
            if ind == currmax:  ret += 1
        return ret