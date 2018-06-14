class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        ret, max_val, min_val = 0, arrays[0][-1], arrays[0][0]
        for i in range(1, len(arrays)):
            ret = max([ret, max_val - arrays[i][0], arrays[i][-1] - min_val])
            max_val = max(max_val, arrays[i][-1])
            min_val = min(min_val, arrays[i][0])
        return ret