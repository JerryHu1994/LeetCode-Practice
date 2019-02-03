class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dic = collections.defaultdict(int)
        curr, ans = 0, 0
        dic[0] = 1
        for val in A:
            curr += val
            ans += dic[curr%K]
            dic[curr%K] += 1
        return ans