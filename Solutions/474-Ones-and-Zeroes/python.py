class Solution(object):
    def count(self, s):
        ret = 0
        for i in s:
            if i=="0":
                ret += 1
        return ret, len(s)-ret
    
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[0]*(n+1) for k in range(m+1)]
        h, w = m, n
        for s in strs:
            zeros, ones = self.count(s)
            for i in range(h,zeros-1,-1): # zeros
                for j in range(w, ones-1, -1): # ones
                    arr[i][j] = max(arr[i][j], 1+arr[i-zeros][j-ones])
        return arr[-1][-1]