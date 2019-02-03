class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sorted_pairs = sorted(pairs, key = lambda x:[x[1], x[0]])
        ret, curr = 1, sorted_pairs[0]
        for p in sorted_pairs[1:]:
            if p[0] > curr[1]:
                curr = p
                ret += 1
        return ret