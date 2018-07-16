class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pq = []
        h, w = len(matrix), len(matrix[0])
        for i in range(h):
            for j in range(w):
                pq.append(matrix[i][j])
        heapq.heapify(pq)
        ret = 0
        for i in range(k):
            ret = heapq.heappop(pq)
        return ret
        
        