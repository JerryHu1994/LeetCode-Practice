class Solution(object):
    
    def helper(self, l1, l2, l3, valid):
        check = True
        currarr = []
        currarr += l1
        currarr += l2
        currarr += l3
        print l1, l2, l3
        for i in currarr:
            if i not in valid:  return False
        if len(set(currarr)) != 9 or sum(currarr) != 45:  return False
        currmatrix = [l1, l2, l3]
        for i in currmatrix:
            if sum(i) != 15:    return False
        for i in zip(*currmatrix):
            if sum(i) != 15:    return False
        if currarr[0] + currarr[4] + currarr[8] != 15 or currarr[2] + currarr[4] + currarr[6] != 15:
            return False
        return True
    
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        valid = set([1,2,3,4,5,6,7,8,9])
        count = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                if self.helper(grid[row][col:col+3], grid[row+1][col:col+3], grid[row+2][col:col+3], valid):
                    count += 1
        return count