class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        heap = []
        for key, v in dic.iteritems():
            heap.append((-v, key))
        heapq.heapify(heap)
        ret = []
        for i in range(k):
            curr = heapq.heappop(heap)
            ret.append(curr[1])
        return ret