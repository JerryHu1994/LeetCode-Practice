class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ret = 0
        currleft = 0
        for c in S:
            if c == "(":
                currleft += 1
            else:
                currleft -= 1
            if currleft < 0:
                ret += -currleft
                currleft = 0
        return ret + currleft