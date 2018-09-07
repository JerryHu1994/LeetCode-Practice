class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        dic = collections.defaultdict(set)
        dic[currval].add(1)
        currstart, currval = 0, p[0]
        for i in range(1, len(p)):
            # check if connected
            if ord(p[i]) - ord(p[i-1]) == 1 or (p[i] == "a" and p[i-1] == "z"):
                dic[currval].add(i-currstart+1)
            else:
                currstart, currval = i, p[i]
                dic[currval].add(1)
        ret = sum(dic.values())
        return ret