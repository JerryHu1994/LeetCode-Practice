class Solution:
    
    def helper(self, board, player):
        for i in range(3):
            arr = [board[i][j] == player for j in range(3)]
            if all(arr):
                return True
            arr = [board[j][i]==player for j in range(3)]
            if all(arr):  
                return True
            if board[0][0] == board[1][1] == board[2][2] == player:
                return True
            if board[0][2] == board[1][1] == board[2][0] == player:
                return True
            return False
    
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        playerx_win = self.helper(board, 'X')
        playero_win = self.helper(board, 'O')
        x_count = sum([s.count('X') for s in board])
        o_count = sum([s.count('O') for s in board])
        if playerx_win and playero_win:
            return False
        if playerx_win and not playero_win and x_count != o_count+1:
            return False
        if not playerx_win and playero_win and x_count != o_count:
            return False
        if not playerx_win and not playero_win:
            if x_count == o_count+1 or x_count == o_count:
                return True
            else:
                return False
        return True