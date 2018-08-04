class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        for i in range(len(expression)-1, -1, -1):
            curr = expression[i]
            if len(stack) and stack[-1]=="?":
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                if curr == "T":
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(curr)
        return stack[-1]