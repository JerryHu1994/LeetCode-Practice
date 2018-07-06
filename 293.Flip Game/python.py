class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        for ind, val in enumerate(s):
            if ind == len(s)-1: continue
            if val=="+" and s[ind+1]=="+":
                ret.append(s[0:ind] + "--" + s[ind+2:])
        return ret