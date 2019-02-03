class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        height, width, ret = len(board), len(board[0]), 0
        for i in range(height):
            for j in range(width):
                # check symbol
                if board[i][j] == '.':  continue
                # check upper
                if i > 0:
                    if board[i-1][j] == 'X':
                        continue
                if j > 0:
                    if board[i][j-1] == 'X':
                        continue
                ret += 1
        return ret