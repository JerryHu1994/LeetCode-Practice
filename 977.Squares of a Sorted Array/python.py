class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A)-1
        ans = []
        while left <= right:
            if A[left]**2 >= A[right]**2:
                ans.append(A[left]**2)
                left += 1
            else:
                ans.append(A[right]**2)
                right -= 1
        return ans[::-1]