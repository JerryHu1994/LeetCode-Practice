class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        wq = sorted([(float(wage[i])/float(quality[i]), quality[i]) for i in range(len(quality))])
        heap, ret, qsum = [], float("inf"), 0
        for ind, val in enumerate(wq):
            r,q = val
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                ret = min(qsum*r, ret)
        return ret