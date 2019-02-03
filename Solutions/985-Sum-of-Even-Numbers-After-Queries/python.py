class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        currsum = sum([i for i in A if i%2 == 0])
        for val, ind in queries:
            if A[ind]%2 == 0:  currsum -= A[ind]
            A[ind] = A[ind] + val
            if A[ind]%2 == 0:  currsum += A[ind]
            ans.append(currsum)
        return ans