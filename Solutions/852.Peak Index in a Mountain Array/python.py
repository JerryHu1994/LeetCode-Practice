class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A)-1
        while left < right:
            mid = (left+right)//2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            if A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                left = mid+1
            if A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                right = mid-1
        return left