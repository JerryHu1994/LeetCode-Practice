class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = [-1]
        for ind,val in enumerate(s):
            if val == "(":
                stack.append(ind)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(ind)
                maxlen = max(ind-stack[-1],maxlen)
        return maxlen
                
                    