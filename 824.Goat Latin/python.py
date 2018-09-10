class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        wordlist = S.split()
        ret = []
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        for ind, w in enumerate(wordlist):
            if w[0].lower() in vowel:
                ret.append(w + "ma" + "a"*(ind+1))
            else:
                ret.append(w[1:] + w[0] + "ma" + "a"*(ind+1))
        return " ".join(ret)