class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        height, width = len(board), len(board[0])
        valid = False
        # horizontally
        for i in range(height):
            for j in range(width-2):
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]) != 0:
                    board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])
                    valid = True
        # vertically
        for i in range(width):
            for j in range(height-2):
                if abs(board[j][i]) == abs(board[j+1][i]) == abs(board[j+2][i]) != 0:
                    board[j][i] = board[j+1][i] = board[j+2][i] = -abs(board[j][i])
                    valid = True
        # shift elements down
        for i in range(width):
            ind = 0
            validlist = []
            for j in range(height-1, -1, -1):
                if board[j][i] > 0:
                    validlist.append(board[j][i])
            while ind < height:
                if ind < len(validlist):
                    board[height-1-ind][i] = validlist[ind]
                else:
                    board[height-1-ind][i] = 0
                ind += 1
        return self.candyCrush(board) if valid else board