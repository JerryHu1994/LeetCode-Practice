class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.ans = 0
        rookx, rooky = 0, 0
        height, width = len(board), len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    rookx, rooky = j, i
        def helper(dy, dx):
            curry, currx = rooky, rookx
            while 0 <= curry < height and 0 <= currx < width and board[curry][currx] != "B":
                if board[curry][currx] == "p":
                    self.ans += 1
                    break
                curry, currx = curry+dy, currx+dx
        for diry, dirx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            helper(diry, dirx)
        return self.ans