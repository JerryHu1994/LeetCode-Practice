class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.matrix = [[False]*n for i in range(n)]
        self.status = 0
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.matrix[row][col] = player
        # check row
        for i in range(self.n):
            if not self.matrix[row][i] == player:
                break
            if i == self.n - 1:
                self.status = player
                return self.status
        
        # check col
        for i in range(self.n):
            if not self.matrix[i][col] == player:
                break
            if i == self.n - 1:
                self.status = player
                return self.status
            
        # diagonal left to right
        if row == col:
            for i in range(self.n):
                if not self.matrix[i][i] == player:
                    break
                if i == self.n - 1:
                    self.status = player
                    return self.status

        # diagonal right to left
        if row + col == self.n - 1:
            currrow, currcol = 0, self.n - 1
            for i in range(self.n):
                if not self.matrix[currrow][currcol] == player:
                    break
                if i == self.n - 1:
                    self.status = player
                    return self.status
                currrow += 1
                currcol -= 1

        return self.status

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)