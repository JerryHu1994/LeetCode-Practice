class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                groups[-1] += 1
            else:
                groups.append(1)
        ret = 0
        for i in range(1, len(groups)):
            ret += min(groups[i-1], groups[i])
        return ret