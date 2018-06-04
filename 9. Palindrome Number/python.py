class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numstr = str(x)
        left, right = 0, len(numstr)-1
        while True:
            if left >= right:
                break
            if numstr[left] != numstr[right]:
                return False
            left += 1
            right -= 1
        return True