class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in t:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in s:
            dic[i] -= 1
        for pair in dic.items():
            if pair[1]:
                return pair[0]
        return 0