class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MIN, MAX = -2**31, 2**31-1
        sign = ((dividend > 0) and (divisor > 0)) or ((dividend < 0) and (divisor < 0))
        dividend, divisor = abs(dividend), abs(divisor)
        sign = 1 if sign else -1
        if dividend < divisor:  return 0
        curr = divisor
        ind = 1
        while True:
            if curr+curr > dividend:    break
            curr += curr
            ind += ind
        ret = sign*(ind + self.divide(dividend - curr, divisor))
        if ret > MAX:
            return MAX
        elif ret < MIN:
            return MIN
        else:
            return ret
            