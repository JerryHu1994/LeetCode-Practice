class Solution(object):
    def dfs(self, i, num, ret):
        if i <= num:
            ret.append(i)
        else:
            return
        nextnum = i*10
        if nextnum <= num:
            for j in range(10):
                self.dfs(nextnum+j,num,ret)
            
    
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [] 
        for i in range(1,10):
            self.dfs(i, n, ret)
        return ret