class Solution(object):
    
    def helper(self, A, B, k):
        la, lb = len(A), len(B)
        if la > lb:
            return self.helper(B, A, k)
        if la == 0: return B[k-1]
        if k == 1:  return min(A[0], B[0])
        ptra = min(k/2, la)
        ptrb = k - ptra
        if A[ptra - 1] <= B[ptrb - 1]:
            # ptra is too small, move right
            return self.helper(A[ptra:], B, ptrb)
        else:
            # ptrb too small, move right
            return self.helper(A, B[ptrb:], ptra)
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        la, lb = len(nums1), len(nums2)
        if (la + lb)%2:
            return self.helper(nums1, nums2, (la+lb)/2+1)
        else:
            return float(self.helper(nums1, nums2, (la+lb)/2) + self.helper(nums1, nums2, (la+lb)/2+1))/2