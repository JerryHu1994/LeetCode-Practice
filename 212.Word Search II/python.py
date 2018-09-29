class Node(object):
    def __init__(self):
        self.children = {}
        self.words = []
    
class Solution(object):
    
    def insert(self, word, trie):
        curr = trie
        for ind, c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = Node()  
            curr = curr.children[c]
        curr.words.append(word)
    
    def dfs(self, board, y, x, trie):
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or board[y][x] == None or board[y][x] not in trie.children:  return
        currval = board[y][x]
        if len(trie.children[currval].words) != 0:
            for w in trie.children[currval].words: self.ret.add(w)
        board[y][x] = None
        self.dfs(board, y-1, x, trie.children[currval])
        self.dfs(board, y, x-1, trie.children[currval])
        self.dfs(board, y, x+1, trie.children[currval])
        self.dfs(board, y+1, x, trie.children[currval])
        board[y][x] = currval
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0:   return []
        height, width = len(board), len(board[0])
        trie = Node()
        self.ret = set()
        # add for words to the dic
        for w in words: self.insert(w, trie)
        for i in range(height):
            for j in range(width):
                self.dfs(board, i, j, trie)
        return list(self.ret)