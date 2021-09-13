class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def caldis(srcx, srcy, destx, desty):
            xdis, ydis = abs(srcx - destx), abs(srcy - desty)
            return max(xdis, ydis)
        ans = 0
        for i in range(len(points) - 1):
            ans += caldis(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
        return ans