class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0: return "-"+self.convertToBase7(-num)
        if num < 7: return str(num)
        left = int(math.ceil(math.log(num)/math.log(7)))
        ret = ""
        for i in range(left, -1, -1):
            currdiv = 7**i
            div = num // currdiv
            ret += str(div)
            num -= div * currdiv
        return ret.lstrip("0")