class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        currdigit, currcnt, cnt = 1, 9, 0
        while cnt + currdigit*currcnt < n:
            cnt += currdigit*currcnt
            currdigit += 1
            currcnt *= 10
        remain = n - cnt - 1
        numoffset, numidx = remain / currdigit, remain % currdigit
        base = 10**(currdigit-1)
        return int(str(base+numoffset)[numidx])
        