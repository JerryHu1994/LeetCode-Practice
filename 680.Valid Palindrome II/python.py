class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left<right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                removeleft = s[left+1: right+1]
                removeleftr = removeleft[::-1]
                removeright = s[left: right]
                removerightr = removeright[::-1]
                return removeleft==removeleftr or removeright==removerightr
        return True