class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(" ")
        if len(str) == 0:   return 0
        sign = 1
        if not str[0].isnumeric():
            if str[0] == "+":
                sign = 1
                str = str[1:]
            elif str[0] == "-":
                sign = -1
                str = str[1:]
            else:
                return 0
        if len(str) == 0:   return 0
        num = None
        for ind, val in enumerate(str):
            if not val.isnumeric():
                num = str[:ind]
                break
        num = str if num == None else num
        if len(num) == 0:   return 0
        num = sign*int(num)
        if num > 2**31 - 1:   return 2**31 - 1
        if num < -2**31:    return -2**31
        return num