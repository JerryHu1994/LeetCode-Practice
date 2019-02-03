class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in xrange(2*len(s)-1):
            if i % 2 ==0 :
                # mid on a number
                left, right = i/2, i/2
            else:
                # mid on empty
                left, right = (i-1)/2, (i+1)/2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        return cnt