class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        l_A, l_B = A.split(), B.split()
        set_A = set(l_A)
        set_B = set(l_B)
        entire = set_A.union(set_B)
        ret = []
        for i in entire:
            if l_A.count(i) == 1 and i not in set_B:
                ret.append(i)
            if i not in set_A and l_B.count(i) == 1:
                ret.append(i)
        return ret