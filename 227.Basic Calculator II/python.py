class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack,res, sign, i = [], 0, "", 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i+1 < len(s) and s[i+1].isdigit():
                    i+=1
                currnum = int(s[start : i+1])
                if sign == "*":
                    stack[-1] *= currnum
                elif sign == "/":
                    stack[-1] = stack[-1] // currnum
                else:
                    stack.append(currnum)
            if s[i] == "+" or s[i] == "-":
                stack.append(s[i])
                sign = s[i]
            if s[i] == "*" or s[i] == "/":
                sign = s[i]
            i += 1
        sign = 1
        for i in range(len(stack)):
            if i%2 == 0:
                res += sign*stack[i]
            else:
                sign = 1 if stack[i] == "+" else -1
        return res