class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        keys = "".join([i.upper() for i in S.split("-")])
        ret = []
        while len(keys) >= K:
            ret.append(keys[-K:])
            keys = keys[:-K]
        if len(keys):   ret.append(keys)
        return "-".join(ret[::-1])
        
            
        