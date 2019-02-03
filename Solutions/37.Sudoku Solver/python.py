class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(board, r, c, char):
            for i in range(9):
                if board[r][i] == char: return False
                if board[i][c] == char: return False
                if board[3*(r/3)+i/3][3*(c/3)+i%3] == char: return False
            return True
        
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in range(1, 10):
                            strval = str(k)
                            if isValid(board, i, j, strval):
                                board[i][j] = strval
                                if dfs(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        dfs(board)