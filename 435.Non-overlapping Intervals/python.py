# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        ret = 0
        sortedint = sorted(intervals, key = lambda x: [x.start, x.end])
        i = 1
        while i < len(sortedint):
            prev, curr = sortedint[i-1], sortedint[i]
            if curr.start < prev.end:
                if curr.end < prev.end:
                    sortedint.pop(i-1)   
                else:    
                    sortedint.pop(i)
                ret += 1
                continue
            i += 1
        return ret
        