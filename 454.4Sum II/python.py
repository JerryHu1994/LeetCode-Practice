class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash1, ret = {}, 0
        for i in A:
            for j in B:
                if i+j in hash1:
                    hash1[i+j] += 1
                else:
                    hash1[i+j] = 1
        for i in C:
            for j in D:
                if -i-j in hash1:
                    ret += hash1[-i-j]
        return ret