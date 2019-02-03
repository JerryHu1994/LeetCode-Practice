class Solution(object):
    def isValid(self, main, small):
        for key in small:
            if key not in main or main[key] < small[key]:
                return False
        return True
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)==0 or len(s)==0:  return ""
        left, right = 0, 0
        ret = float("inf")
        retstr = ""
        sourceHash, targetHash = collections.defaultdict(int), collections.Counter(t)
        
        for left in range(len(s)):
            #print left, s[left:right]
            while right < len(s) and not self.isValid(sourceHash, targetHash):
                # move right
                sourceHash[s[right]] += 1
                if right < len(s):
                    right += 1
                else:
                    break
            if self.isValid(sourceHash, targetHash):
                ret = min(ret, right - left)
                if right - left <= ret:
                    retstr = s[left:right] 
            sourceHash[s[left]] -= 1
        return retstr