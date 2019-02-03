class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        ret = 0
        cnt = 0
        for ind,val in enumerate(S):
            if val == "(":
                cnt += 1
            else:
                cnt -= 1
            if val==")" and S[ind-1] == "(":
                ret += 1<<cnt
        return ret