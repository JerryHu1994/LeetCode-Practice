class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)
        comp = "0b"
        for i in b[2:]:
            if i=="1":
                comp+="0"
            else:
                comp+="1"
        return int(comp, 2)