class Solution(object):
    
    def helper(self, S):
        if len(S)==0:
            return [""]
        ret = []
        val = S[0]
        if val.isalpha():
            low = val.lower()
            high = val.upper()
            for i in self.helper(S[1:]):
                ret.append(low+i)
            for i in self.helper(S[1:]):
                ret.append(high+i)
        else:
            for i in self.helper(S[1:]):
                ret.append(val+i)
        return ret
    
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0: return [""]
        return self.helper(S)
        
        