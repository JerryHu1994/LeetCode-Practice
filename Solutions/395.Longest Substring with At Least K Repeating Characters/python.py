class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c = collections.Counter(s)
        prev, currmax = 0, 0
        flag = True
        for i in range(len(s)):
            if c[s[i]] < k:
                currmax = max(currmax, self.longestSubstring(s[prev:i], k))
                prev = i+1
                flag = False
        # if all valid, just return the length
        if flag:
            return len(s)
        return max(currmax, self.longestSubstring(s[prev:len(s)], k))
        
                