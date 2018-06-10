class Solution(object):
    
    def helper(self, direction, row, col):
        if direction == "right":  col+=1
        if direction == "down":   row+=1
        if direction == "left":   col-=1
        if direction == "up":   row-=1
        return row, col
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:  return []
        r, c = 0, 0
        m, n = len(matrix), len(matrix[0])
        visited = [[False]*n for i in range(m)]
        currdir = "right"
        order_map = {"right":"down", "down": "left", "left":"up", "up":"right"}
        ret = []
        for i in range(m*n):
            ret.append(matrix[r][c])
            visited[r][c] = True
            nextr, nextc = self.helper(currdir, r, c)
            # check if next is visited
            if nextr >= 0 and nextr < m and nextc >= 0 and nextc < n and not visited[nextr][nextc]:
                r, c = nextr, nextc # good to go 
            else:
                # turn clockwise
                currdir = order_map[currdir]
                r, c = self.helper(currdir, r, c)
        return ret