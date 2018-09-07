class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:    return "0"
        if num < 0: num += 2 ** 32
        hex = "0123456789abcdef"
        leftmost = int(math.ceil(math.log(num)/math.log(16)))
        ret = ""
        while leftmost >= 0:
            div = num//(16**leftmost)
            num = num%(16**leftmost)
            leftmost -= 1
            ret += str(hex[div])
        return ret.lstrip("0")