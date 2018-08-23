class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        for ind, val in enumerate(B):
            dic[val].append(ind)
        ret = []
        for i in A:
            ret.append(dic[i].pop(0))
        return ret