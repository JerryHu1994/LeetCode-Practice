class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left, right = 1, m*n
        while left < right:
            cnt, mid = 0, (left+right)/2
            for i in range(1,m+1):
                cnt += n if i*n <= mid else mid//i
            if cnt < k:
                left = mid+1
            else:
                right = mid
        return left