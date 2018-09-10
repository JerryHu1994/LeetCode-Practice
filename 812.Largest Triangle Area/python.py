class Solution(object):
    def area(self, p):
        a,b,c = p
        return 0.5*abs(a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - b[0]*a[1] - c[0]*b[1] - a[0]*c[1])
        
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return max([self.area(p) for p in itertools.combinations(points, 3)])