class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = collections.defaultdict(int)
        if len(s) < 10: return []
        for i in range(0, len(s)-9):
            dic[s[i:i+10]] += 1
        ret = []
        for k,v in dic.iteritems():
            if v > 1:   ret.append(k)
        return ret