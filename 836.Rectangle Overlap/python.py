class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        r1x1, r1y1, r1x2, r1y2 = rec1
        r2x1, r2y1, r2x2, r2y2 = rec2
        return False if r2x1 >= r1x2 or r2y1 >= r1y2 or r2x2 <= r1x1 or r2y2 <= r1y1 else True