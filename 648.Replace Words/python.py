class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dicts = set(dict)
        wordlist = sentence.split()
        for ind,w in enumerate(wordlist):
            for i in range(len(w)):
                if w[:i+1] in dicts:
                    wordlist[ind] = w[:i+1]
                    break
        return " ".join(wordlist)
                    