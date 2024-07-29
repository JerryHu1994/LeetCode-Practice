class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for o in ops:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1]*2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        return sum(stack)