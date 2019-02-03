# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        while len(A) > 0 and len(B) > 0:
            if A[0].end < B[0].start:
                A.pop(0)
            elif B[0].end < A[0].start:
                B.pop(0)
            else:
                if A[0].start < B[0].start:
                    ans.append(Interval(B[0].start, min(A[0].end, B[0].end)))
                    if A[0].end > B[0].end:
                        B.pop(0)
                    else:
                        A.pop(0)
                else:
                    ans.append(Interval(A[0].start, min(A[0].end, B[0].end)))
                    if A[0].end > B[0].end:
                        B.pop(0)
                    else:
                        A.pop(0)
        return ans