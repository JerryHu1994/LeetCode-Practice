class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        pts = [p1, p2, p3, p4]
        pts = sorted(pts, key = lambda x: (x[0], x[1]))
        dis = lambda x, y:(x[0]-y[0])**2 + (x[1]-y[1])**2
        return dis(pts[0], pts[1]) == dis(pts[0], pts[2]) != 0 and dis(pts[2], pts[1]) == dis(pts[0], pts[3]) != 0