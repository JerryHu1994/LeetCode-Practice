# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # find the last interval whose end is before newInterval start
        endlist = [i.end for i in intervals]
        before = bisect.bisect_left(endlist, newInterval.start)
        
        # find the first interval whose start is after newInterval end
        startlist = [i.start for i in intervals]
        after = bisect.bisect_right(startlist, newInterval.end)
        start, end = 0, 0

        if before == after:
            # no overlap
            start, end = newInterval.start, newInterval.end
        else:
            start, end = min(intervals[before].start, newInterval.start), max(intervals[after-1].end, newInterval.end)
        return intervals[:before] + [[start, end]] + intervals[after:]
        