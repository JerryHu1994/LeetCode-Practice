class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        ts = []
        for p in timePoints:
            h, m = int(p.split(":")[0]), int(p.split(":")[1])
            ts.append(60*h+m)
        ts = sorted(ts)
        ret = 24*60
        for i in range(0, len(ts)-1):
            ret = min(ret, ts[i+1]-ts[i])
        ret = min(ret, ts[0]+24*60 - ts[-1])
        return ret
            