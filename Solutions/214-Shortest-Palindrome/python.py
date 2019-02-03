class Solution(object):
    def isPalin(self, s):
        for i in range(len(s)//2):
            if s[i] == s[len(s)-1]:
                return False
        return True
    
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        prelist = []
        ptr = len(s)-1
        if self.isPalin(s): return s
        while True:
            prelist.add(s[ptr])
            currstr = "".join(prelist)+s
            if self.isPalin(currstr):
                return True
            ptr -= 1