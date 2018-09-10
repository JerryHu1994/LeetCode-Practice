class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jset = set([i for i in J])
        ret = 0
        for i in S:
            if i in jset:
                ret += 1
        return ret