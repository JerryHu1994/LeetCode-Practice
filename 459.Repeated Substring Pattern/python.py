class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)/2+1):
            currstr = s[0:i]
            if len(s)%i != 0:
                continue
            for j in range(len(s)/i):
                if s[j*i:(j+1)*i] != currstr:
                    break
                if j == len(s)/i-1:
                    return True
        return False