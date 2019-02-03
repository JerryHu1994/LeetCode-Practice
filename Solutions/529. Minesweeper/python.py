class Solution(object): 
    def getMine(self, board, y, x, height, width):
        adjs_coods = [(y-1,x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
        adjs_coods = [board[c[0]][c[1]] for c in adjs_coods if 0<=c[0]<=height-1 and 0<=c[1]<=width-1]
        return adjs_coods.count('M')

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        height, width = len(board), len(board[0])
        sym = board[click[0]][click[1]]
        if sym == "M":
            board[click[0]][click[1]] = 'X'
            return board
        else:
            stack = [(click[0], click[1])]
            while len(stack):
                curr = stack.pop()
                y,x = curr
                cnt = self.getMine(board, y, x, height, width)
                if cnt == 0:
                    board[y][x] = "B"
                    adjs_coods = [(y-1,x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
                    adjs_coods = [c for c in adjs_coods if 0<=c[0]<=height-1 and 0<=c[1]<=width-1 and board[c[0]][c[1]] == "E"]
                    stack.extend(adjs_coods)
                else:
                    board[y][x] = str(cnt)
        return board
            
            
            