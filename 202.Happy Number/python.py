class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        s = set()
        while True:
            currlist = [int(i) for i in str(num)]
            currsum = 0
            for i in currlist:
                currsum += i**2
            if currsum in s:
                return False
            elif currsum == 1:
                return True
            else:
                s.add(currsum)
            num = currsum
        return True
            