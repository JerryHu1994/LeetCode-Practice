class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head, step, left, remaining = 1, 1, True, n
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            left, step, remaining = not left, step*2, remaining/2
        return head