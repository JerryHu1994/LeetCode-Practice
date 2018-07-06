class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        curr_r, curr_c = m, n
        for o in ops:
            curr_r = min(curr_r, o[0])
            curr_c = min(curr_c, o[1])
        return curr_r*curr_c