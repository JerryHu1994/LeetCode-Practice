class Solution(object):
    
    def dfs(self, board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == ".":
                    found = False
                    for i in range(1,10):
                        currval = str(i)
                        if self.isValid(board, y, x, currval):
                            board[y][x] = currval
                            if self.dfs(board):
                                return True
                            else:
                                board[y][x] = "."
                    return False
        return True

    def isValid(self, board, r, c, char):
        for i in range(9):
            if board[r][i] == char: return False
            if board[i][c] == char: return False
            if board[3*(r/3)+i/3][3*(c/3)+i%3] == char: return False
        return True
        
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:   return False
        self.dfs(board)
                