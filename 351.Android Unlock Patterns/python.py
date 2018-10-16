class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.jump = {(1,3) : 2, (3,1) : 2, (1, 7) : 4, (7,1) : 4, (3, 9):6, (9,3): 6, (7,9) : 8, (9,7) : 8,
                    (2, 8) : 5, (8,2) :5, (4,6):5, (6,4) : 5, (1,9):5, (9,1):5, (3,7):5, (7,3):5}
        def helper(m, n, currnum, visited, currlen, res):
            if m <= currlen <= n:   res += 1
            currlen += 1
            if currlen > n:   return res
            visited[currnum-1] = True
            for i in range(1,10):
                if visited[i-1] or ((currnum, i) in self.jump and not visited[self.jump[(currnum, i)]-1]):
                    continue
                else:
                    res = helper(m, n, i, visited, currlen, res)
            visited[currnum-1] = False
            return res
        ret = 0                
        ret += helper(m, n, 1, [False]*9, 1, 0)*4
        ret += helper(m, n, 2, [False]*9, 1, 0)*4
        ret += helper(m, n, 5, [False]*9, 1, 0)
        return ret