class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        l = len(A)
        A, pairsB = sorted(A), sorted([(val, ind) for ind, val in enumerate(B)])
        ret = [None]*l
        ptrA, ptrB = 0, 0
        unused = []
        while ptrA < l and ptrB < l:
            if A[ptrA] > pairsB[ptrB][0]:
                ret[pairsB[ptrB][1]] = A[ptrA]
                ptrA += 1
                ptrB += 1
            else:
                unused.append(A[ptrA])
                ptrA += 1
        ptrA  = 0
        for ind, val in enumerate(ret):
            if val == None:
                ret[ind] = unused[ptrA]
                ptrA += 1
        return ret