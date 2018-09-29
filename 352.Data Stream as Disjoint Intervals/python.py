# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        self.s = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.s:   return
        self.s.add(val)
        newinterval = [val, val]
        startidx = [i[1] for i in self.intervals]
        find = bisect.bisect_right(startidx, val)
        if find > 0 and find < len(self.intervals):
            # merge two intervals
            ##print self.intervals
            if val == self.intervals[find-1][1] + 1 == self.intervals[find][0] - 1:
                self.intervals[find-1][1] = self.intervals[find][1]
                self.intervals.pop(find)
                return
        # merge the one before
        if find > 0 and self.intervals[find-1][1]+1 == val:
            self.intervals[find-1][1] = val
            return
        # merge the one after
        if find < len(self.intervals) and self.intervals[find][0] - 1 == val:
            self.intervals[find][0] = val
            return
        self.intervals.insert(find, newinterval)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()