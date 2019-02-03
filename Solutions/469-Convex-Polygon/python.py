class Solution(object):
    def crossproduct(self, x1, y1, x2, y2):
        return x1*y2 - y1*x2
    
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        l = len(points)
        sign = 0
        for i in range(l):
            pa, pb, pc = points[i%l], points[(i+1)%l], points[(i+2)%l]
            cp = self.crossproduct(pa[0]-pb[0], pa[1]-pb[1], pc[0]-pb[0], pc[1]-pb[1])
            if not sign:
                sign = cp
            else:
                if cp * sign < 0:
                    return False
        return True