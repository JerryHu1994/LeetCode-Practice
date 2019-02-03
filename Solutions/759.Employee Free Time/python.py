# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        points, ret = [], []
        for person in schedule:
            for s in person:
                points.append((s.start, 1)) # 1 for busy
                points.append((s.end, 0)) # 0 for not busy
        points = sorted(points)
        # sweep
        currscore, currstart = 0, None
        for p in points:
            if currscore == 0 and currstart != None and currstart != p[0]:
                ret.append(Interval(currstart, p[0]))
            if p[1] == 1:
                currscore += 1
            else:
                currscore -= 1
            currstart = p[0]
        return ret
            
            
        