class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        ans = 0
        currmax = 0
        for l,w in rectangles:
            if min(l, w) > currmax:
                currmax = min(l, w)
                ans = 1
            elif min(l, w) == currmax:
                ans += 1
        return ans