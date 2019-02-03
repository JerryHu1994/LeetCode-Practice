class Solution(object):
    def isValid(self, prevpos, currrow, currcol):
        for r, c in enumerate(prevpos):
            if c == currcol or abs(r-currrow) == abs(c-currcol):
                return False
        return True
    
    def helper(self, rowidx, currpos, n):
        if rowidx == n:
            # found a solution, let's add it
            sol = []
            for col in currpos:
                sol.append("."*col+"Q"+"."*(n-col-1))
            self.ret.append(sol)
            
        for i in range(n):
            if self.isValid(currpos, rowidx, i):
                self.helper(rowidx+1, currpos + [i], n)
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ret = []
        self.helper(0, [], n)
        return self.ret