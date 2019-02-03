class Solution(object):
    
    def isPalin(self, s):
        return s==s[::-1]
    
    def dfs(self, s, strlist):
        if len(s)==0:
            Solution.res.append(strlist)
        for i in range(1,1+len(s)):
            if self.isPalin(s[:i]):
                self.dfs(s[i:], strlist+[s[:i]])
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.res = []
        self.dfs(s,[])
        return Solution.res    