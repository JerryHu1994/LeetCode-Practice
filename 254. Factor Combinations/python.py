class Solution(object):
    
    def helper(self, n, currfac, currlist):
        if n < currfac: return
        found = False
        if len(currlist) != 0:
            if currlist + [n] not in self.ret:
                self.ret.append(currlist + [n])
        for i in range(currfac, int(math.sqrt(n))+1):
            if n%i == 0:
                self.helper(n/i, i, currlist + [i])
                found = True
        if not found:
            if len(currlist) == 0:  return
            if currlist + [n] not in self.ret:
                self.ret.append(currlist + [n])
    
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.helper(n, 2, [])
        return self.ret
            