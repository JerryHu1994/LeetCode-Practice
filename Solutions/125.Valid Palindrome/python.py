class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = [i.lower() for i in s if i.isalnum()]
        return li == li[::-1]
        
            
            
        
        