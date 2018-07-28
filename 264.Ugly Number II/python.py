from heapq import *
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = []
        s = set()
        heappush(heap, 1)
        s.add(1)
        for i in range(n-1):
            curr = heappop(heap)
            if curr*2 not in s:
                heappush(heap, curr*2)
                s.add(curr*2)
            if curr*3 not in s:
                heappush(heap, curr*3)
                s.add(curr*3)
            if curr*5 not in s:
                heappush(heap, curr*5)
                s.add(curr*5)
        return heappop(heap)