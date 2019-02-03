class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        se = set()
        left, right, ret = 0, 0, 0
        while left<len(s) and right < len(s):
            if s[right] in se:
                while s[left]!=s[right]:
                    se.remove(s[left])
                    left+=1
                left+=1
            else:
                se.add(s[right])
                ret = max(ret, right-left+1)
            right+=1
        return ret
        
        