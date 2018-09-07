class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        sorted_A, set_A = sorted(A), set(A)
        dic = collections.defaultdict(int)
        for ind, val in enumerate(sorted_A):
            dic[val] = 1
            for i in range(0, ind):
                if val % sorted_A[i] == 0 and val / sorted_A[i] in set_A:
                    dic[val] += dic[sorted_A[i]] * dic[val/sorted_A[i]]
            dic[val] = dic[val] % MOD
        ret = sum([i for i in dic.values()])
        return ret % MOD