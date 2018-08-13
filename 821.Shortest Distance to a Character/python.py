class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        curr = None
        ret = [float("inf")]*len(S)
        for ind, c in enumerate(S):
            if c == C:
                curr = ind
                ret[ind] = 0
            else:
                if curr != None:
                    ret[ind] = min(ret[ind], ind-curr)
        curr = None
        for ind in range(len(S)-1, -1, -1):
            if S[ind] == C:
                curr = ind
            else:
                if curr != None:
                    ret[ind] = min(curr-ind, ret[ind])
        return ret