class Solution(object):
    def isValid(self, li):
        filtered = []
        for i in li:
            if i != ".":    filtered.append(i)
        return len(filtered) == len(set(filtered))
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for row in board:
            if not self.isValid(row):
                return False
        # check cols
        for col in zip(*board):
            if not self.isValid(list(col)):
                return False
        # check squares
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not self.isValid([board[i][j], board[i][j+1], board[i][j+2], board[i+1][j],board[i+1][j+1], board[i+1][j+2],board[i+2][j],board[i+2][j+1], board[i+2][j+2]]):
                    return False
        return True