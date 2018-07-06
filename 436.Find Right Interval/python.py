# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        index = {}
        for i, v in enumerate(intervals):
            index[v.start] = i
        sorted_int = sorted(intervals, key = lambda x: [x.start, x.end]) # sort by start
        l = len(sorted_int)
        ret = []
        for i in intervals
            start, end = i.start, i.end
            left, right = 0, l-1
            mid = (left + right)/2
            # do binary search
            while left < right:
                if sorted_int[mid].start >= end:
                    right = mid
                else:
                    left = mid+1
                mid = (left + right)/2
            if mid == l-1 and sorted_int[mid].start < end:  
                ret.append(-1)
            else:
                ret.append(index[sorted_int[mid].start])
        return ret
            