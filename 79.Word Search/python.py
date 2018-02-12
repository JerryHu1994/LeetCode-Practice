class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board)==0 or len(board[0])==0:   return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, j,i):
                    return True
        return False
        
        
    def dfs(self, board, word, x, y):
        if len(word)==0:    return True
        if x<0 or x>=len(board[0]) or y<0 or y>=len(board): return False
        if board[y][x]!=word[0]:    return False
        board[y][x] = '0'
        exist = self.dfs(board, word[1:], x-1, y) or self.dfs(board, word[1:], x+1, y) or self.dfs(board, word[1:], x, y-1) or self.dfs(board, word[1:], x, y+1)
        board[y][x] = word[0]
        return exist