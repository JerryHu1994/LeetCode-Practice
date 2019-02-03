class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        pairs = [(val, ind) for ind,val in enumerate(A)]
        pairs = sorted(pairs, key = lambda x:[x[0], x[1]])
        currmin = pairs[0][1]
        for i in range(1, len(pairs)):
            currnum, currind = pairs[i]
            if currind > currmin:
                ans = max(ans, currind - currmin)
            currmin = min(currmin, currind)
        return ans