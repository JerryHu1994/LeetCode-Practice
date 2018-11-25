class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:  return []
        hq = []
        heapq.heappush(hq, (nums1[0]+nums2[0], 0, 0))
        ret = []
        for i in range(k):
            if len(hq) == 0:    break
            currsum, y, x = heapq.heappop(hq)
            ret.append([nums1[y], nums2[x]])
            if x < len(nums2)-1:  heapq.heappush(hq, (nums1[y]+nums2[x+1], y, x+1))
            if x == 0 and y < len(nums1)-1:  heapq.heappush(hq, (nums1[y+1]+nums2[x], y+1, x))
        return ret