class Solution(object):
    def inrange(self, char):
        return ord(char) >= ord("a") and ord(char) <= ord("z")
    
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        first, second, third = True, True, True
        for ind, char in enumerate(word):
            if ind == 0:
                if not self.inrange(char):
                    second = False
                else:
                    first, third = False, False
            else:
                if not self.inrange(char):
                    second,third = False, False
                else:
                    first = False
        return first or second or third
                
        