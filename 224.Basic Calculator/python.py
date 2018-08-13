class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = 1
        res = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i+1<len(s) and s[i+1].isdigit():
                    i += 1 
                currnum = int(s[start:i+1])
                res += sign*currnum
            if c == "+":
                sign = 1
            if c == "-":
                sign = -1
            if c == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            if c == ")":
                presign = stack.pop()
                preres = stack.pop()
                res = presign*res + preres
            i += 1
        return res