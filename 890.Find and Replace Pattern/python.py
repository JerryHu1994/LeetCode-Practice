class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ret = []
        for w in words:
            if len(w) != len(pattern):  continue
            dic = {}
            valid = True
            for ind,val in enumerate(w):
                if val in dic:
                    if dic[val] != pattern[ind]:
                        valid = False
                        break
                else:
                    if pattern[ind] in dic.values():
                        valid = False
                        break
                    else:
                        dic[val] = pattern[ind]
            if valid:   ret.append(w)   
        return ret