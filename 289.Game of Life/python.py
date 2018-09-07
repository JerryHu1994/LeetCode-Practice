class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 0 dead to dead, 1 live to live, 2 dead to live, 3 live to dead
        height, width = len(board), len(board[0])
        for i in range(height):
            for j in range(width):
                cnt = 0
                neighbors = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
                for n in neighbors:
                    if n[0] < 0 or n[0] >= height or n[1] < 0 or n[1] >= width: continue
                    if board[n[0]][n[1]] == 1 or board[n[0]][n[1]] == 3:  cnt += 1
                if board[i][j] == 1:
                    if cnt < 2:
                        board[i][j] = 3
                    elif cnt ==2 or cnt ==3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
                else:
                    if cnt == 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 0
        for i in range(height):
            for j in range(width):
                board[i][j] = 1 if board[i][j] == 1 or board[i][j] == 2 else 0
                    