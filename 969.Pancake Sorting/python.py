class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        ind = len(A)
        while ind > 1:
            max_ind = A[:ind].index(ind)
            if max_ind != 0:
                A = A[:max_ind+1][::-1]+A[max_ind+1:]
                ans.append(max_ind+1)
            A = A[:ind][::-1]+A[ind:]
            ans.append(ind)
            ind -= 1
        return ans