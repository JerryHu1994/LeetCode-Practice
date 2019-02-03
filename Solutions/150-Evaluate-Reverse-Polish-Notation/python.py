class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for ind, val in enumerate(tokens):
            if val == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif val == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif val == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif val == "/":
                second = stack.pop()
                first = stack.pop()
                if first % second == 0:
                    res = first/second
                else:
                    if first // second >=0:
                        res = first // second
                    else:
                        res = first // second + 1
                stack.append(res)
            else:
                currnum = int(val)
                stack.append(currnum)
        return stack[0]