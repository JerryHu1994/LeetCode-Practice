class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        ret, cntB = [], collections.Counter()
        for sB in B:
            for c in set(sB):   cntB[c] = max(cntB[c], sB.count(c))
        for wA in A:
            cntA = collections.Counter(wA)
            valid = True
            for key in cntB:
                if key not in cntA or cntB[key] > cntA[key]:
                    valid = False
                    break
            if valid:   ret.append(wA)
        return ret
            