class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        ret = ""
        pairs = sorted([(indexes[i], sources[i], targets[i]) for i in range(len(indexes))])
        ind = 0
        while ind < len(S):
            if len(pairs) == 0:
                ret += S[ind:]
                break
            if ind == pairs[0][0]:
                currind, currs, currt = pairs.pop(0)
                if S[ind:ind+len(currs)] == currs:
                    ret += currt
                    ind += len(currs)
                else:
                    ret += S[ind]
                    ind += 1
            else:
                ret += S[ind]
                ind += 1
        return ret