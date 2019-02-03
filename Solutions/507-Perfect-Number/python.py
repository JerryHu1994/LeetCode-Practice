class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0: return False
        if num == 1:    return False
        limit = int(math.ceil(math.sqrt(num)))
        s = 1
        for i in range(2, limit):
            if num%i == 0:
                s += i
                s += num/i
        return s==num