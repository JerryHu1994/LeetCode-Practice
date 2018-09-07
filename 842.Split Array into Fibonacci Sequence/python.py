class Solution(object):
    def helper(self, S, prelist):
        if len(S) == 0:
            return prelist if len(prelist) >= 3 else False
        # first and second and element
        if len(prelist) <= 1:
            if S[0] == "0":
                return self.helper(S[1:], prelist+[int(S[0])])
            for i in range(1, len(S)+1):
                ret = self.helper(S[i:], prelist+[int(S[:i])])
                if ret != False:    return ret
        else:
            nextval = str(prelist[-1] + prelist[-2])
            l = len(nextval)
            if S[0] == "0": return self.helper(S[1:], prelist+[0]) if nextval == "0" else False
            if len(S) >= l and S[:l] == nextval and prelist[-1] + prelist[-2] <= 2**31-1:
                return self.helper(S[l:], prelist+[int(S[:l])])
            else:
                ret = False
        return False
    
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ret = self.helper(S, [])
        return ret if ret != False else []