class Solution(object):
    def helper(self, remain, prev, count):
        if len(remain) == 0:
            if count == 4:
                self.ret.append(".".join(prev))
                return
            else:
                return
        if remain[0] == "0":
            self.helper(remain[1:], prev + ["0"], count+1)
            return
        #print remain, prev
        for i in range(min(3,len(remain))):
            if int(remain[0:i+1]) > 255:    continue
            self.helper(remain[i+1:], prev + [remain[0:i+1]], count+1)
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12: return []
        self.ret = []
        self.helper(s, [], 0)
        return self.ret