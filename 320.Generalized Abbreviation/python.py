class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = set()
        def helper(w, prev, flag):
            if len(w) == 0:
                ret.add(prev)
                return
            for i in range(1, len(word)+1):
                if len(prev) == 0:
                    helper(w[i:], prev+str(len(w[:i])), True)
                    helper(w[i:], prev+w[:i], False)
                else:
                    if flag:
                        helper(w[i:], prev+w[:i], False)
                    else:
                        helper(w[i:], prev+str(len(w[:i])), True)
        helper(word, "", None)
        return list(ret)