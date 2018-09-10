class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        alphadic = collections.defaultdict(int)
        for i in licensePlate:
            if i.isalpha(): alphadic[i.lower()] += 1
        retword, retlength = "", float("inf")
        for w in words:
            currdic = collections.defaultdict(int)
            for c in w: currdic[c.lower()] += 1
            valid = True
            for key, val in alphadic.iteritems():
                if key not in currdic or currdic[key] < alphadic[key]:  
                    valid = False
                    break
            if valid and retlength > len(w):
                retlength = len(w)
                retword = w
        return retword