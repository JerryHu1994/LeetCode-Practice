class Solution(object):
    def helper(self,start, end, currlist, count):
        if count == 0:
            self.ret.append(currlist)
        if start>end:
            return
        for i in range(start, end+1):
            self.helper(i+1, end, currlist + [i], count-1)
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.helper(1, n, [], k)
        return self.ret