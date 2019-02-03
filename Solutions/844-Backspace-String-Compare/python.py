class Solution(object):
    def helper(self, S):
        stack = []
        for c in S:
            if c == "#":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(c)
        return stack
    
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return "".join(self.helper(S)) == "".join(self.helper(T))
    