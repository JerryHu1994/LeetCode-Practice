class Solution(object):
    def helper(self, n):
        if n in self.dic:
            return self.dic[n]
        if n==0 or n==1:    return 1
        ret = 0
        for i in range(n):
            ret += self.helper(i)*self.helper(n-1-i)
        if not n in self.dic:
            self.dic[n] = ret
        return ret
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dic = {}
        return self.helper(n)