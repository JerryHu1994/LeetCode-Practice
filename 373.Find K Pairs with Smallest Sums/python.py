class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(heap, [i+j, i, j])
        ret = []
        for i in range(k):
            if len(heap)==0:    return ret
            ret.append(heapq.heappop(heap)[1:])
        return ret
        