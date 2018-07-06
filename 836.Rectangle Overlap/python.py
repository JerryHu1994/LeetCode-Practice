class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec1[3] < rec2[1]:
            return False
        elif rec1[1] < rec2[1] and rec2[1] < rec1[3]:
            if rec2[2] <= rec1[0]:
                return False
            if rec2[0] >= rec1[2]:
                return False
            return True
        else:
            if rec2[3] < rec1[1]:
                return False
            if rec2[2] <= rec1[0]:
                return False
            if rec2[0] >= rec1[2]:
                return False
            return True
            