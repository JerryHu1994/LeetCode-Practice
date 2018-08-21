class Solution(object):
    def isValid(self, prevpos, currrow, currcol):
        for r, c in enumerate(prevpos):
            if c == currcol or abs(r-currrow) == abs(c-currcol):
                return False
        return True
    
    def helper(self, rowidx, currpos, n):
        if rowidx == n:
            # found a solution, let's add it
            self.ret += 1
            
        for i in range(n):
            if self.isValid(currpos, rowidx, i):
                self.helper(rowidx+1, currpos + [i], n)
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ret = 0
        self.helper(0, [], n)
        return self.ret
        