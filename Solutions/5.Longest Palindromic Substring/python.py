class Solution(object):
    def helper(self, s, l, r):
        while l>=0 and r < len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return r-l-1
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0,0
        for i in xrange(len(s)):
            first, second = self.helper(s, i, i), self.helper(s, i, i+1)
            m = max(first, second)
            if m>right-left+1:
                left, right = i - (m-1)/2, i + m/2
        return s[left: right+1]
            