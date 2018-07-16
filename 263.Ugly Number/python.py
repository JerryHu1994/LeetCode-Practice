class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        curr = num
        if curr == 0:   return False
        while curr%2 == 0:
            curr = curr/2
        while curr%3 == 0:
            curr = curr/3
        while curr%5 == 0:
            curr = curr/5
        return True if curr == 1 else False