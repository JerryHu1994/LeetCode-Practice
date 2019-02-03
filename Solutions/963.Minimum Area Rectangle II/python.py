class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ans, st, n = float('inf'), {(x,y)   for x,y in points}, len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    if not (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) and (x3 + (x2 - x1), y3 + (y2 - y1)) in st:
                        ans = min(ans, math.sqrt((x2 - x1)**2 + (y2 - y1)**2) * math.sqrt((x3-x1)**2 + (y3-y1)**2))
        return ans if ans != float('inf') else 0