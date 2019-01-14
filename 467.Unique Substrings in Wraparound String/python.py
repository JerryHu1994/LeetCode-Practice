class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:   return 0
        dic = collections.defaultdict(int)
        cnt = 1
        dic[p[0]] = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i-1])) % 26 == 1:
                cnt += 1
            else:
                cnt = 1
            dic[p[i]] = max(dic[p[i]], cnt)
        return sum(dic.values())