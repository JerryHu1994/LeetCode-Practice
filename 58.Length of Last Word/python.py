class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splited = s.split()
        return len(splited[-1]) if len(splited) != 0 else 0