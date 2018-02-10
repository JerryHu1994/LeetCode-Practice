# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        sortlist = sorted(intervals,key=lambda x: (x.start, x.end))
        curr = None
        for ind,i in enumerate(sortlist):
            if curr==None:
                curr = i
                if ind == len(intervals)-1: ret.append(curr)
                continue
            if i.start >= curr.start and i.start <= curr.end: #can merge
                curr.end = max(curr.end, i.end)
            else: #cannot merge
                ret.append(curr)
                curr = i
            if ind == len(intervals)-1: ret.append(curr)
        
        return ret
            