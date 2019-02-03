class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) < 3 or len(board[1]) < 3:   return
        height, width = len(board), len(board[0])
        visited = [[False]*width for i in range(height)]
        globalstore = []
        for i in range(1, height-1):
            for j in range(1, width-1):
                if board[i][j] == "X" or visited[i][j]:
                    continue
                valid = True
                store = [(j, i)]
                queue = [(j, i)]
                visited[i][j] = True
                while len(queue):
                    currx, curry = queue.pop(0)
                    if currx == 0 or currx == width-1 or curry == 0 or curry == height-1:
                        valid = False
                    if currx > 0 and board[curry][currx-1] == "O" and not visited[curry][currx-1]:
                        queue.append((currx-1, curry))
                        store.append((currx-1, curry))
                        visited[curry][currx-1] = True
                    if currx < width-1 and board[curry][currx+1] == "O" and not visited[curry][currx+1]:
                        queue.append((currx+1, curry))
                        store.append((currx+1, curry))
                        visited[curry][currx+1] = True
                    if curry > 0 and board[curry-1][currx] == "O" and not visited[curry-1][currx]:
                        queue.append((currx, curry-1))
                        store.append((currx, curry-1))
                        visited[curry-1][currx] = True
                    if curry < height-1 and board[curry+1][currx] == "O" and not visited[curry+1][currx]:
                        queue.append((currx, curry+1))
                        store.append((currx, curry+1))
                        visited[curry+1][currx] = True
                # flip the O
                if valid:   globalstore += store
        for c in globalstore:   board[c[1]][c[0]] = "X"