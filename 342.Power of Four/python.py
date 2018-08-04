class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = bin(num)[2:]
        return True if s.count('1')==1 and s.count('0')%2==0 and num > 0 else False