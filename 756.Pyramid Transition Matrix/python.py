class Solution(object):
    
    def dfs(self, bottom, up, dic):
        up_len = len(up)
        if up_len == len(bottom)-1:
            if up_len == 1: return True
            return self.dfs(up, "", dic)
        currbase = bottom[up_len] + bottom[up_len+1]
        currlist = dic[currbase]
        if len(currlist) == 0:  return False
        for val in currlist:
            if self.dfs(bottom, up+val, dic): return True
        return False
    
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        dic = collections.defaultdict(list)
        for p in allowed:
            dic[p[:2]].append(p[2])
        return self.dfs(bottom, "", dic)