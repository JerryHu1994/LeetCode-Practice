class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            dic[i]=dic[i]+1 if i in dic else 1
        odd = False
        for i in dic:
            if dic[i]%2==1:
                if not odd:
                    odd=True
                else:
                    return False
        return True