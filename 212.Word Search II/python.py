class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word = None
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:    return []
        trie = Node()
        # build the trie
        for w in words:
            curr = trie
            for c in w: curr = curr.children[c]
            curr.word = w
        height, width, ret = len(board), len(board[0]), set()
        visited = [[0]*width for i in range(height)]
        def dfs(y, x, visited, curr):
            # check if a word ends here
            if curr.word != None:   ret.add(curr.word)
            if y < 0 or y >= height or x < 0 or x >= width or visited[y][x]:    return
            if board[y][x] not in curr.children:    return
            visited[y][x] = 1
            dfs(y-1, x, visited, curr.children[board[y][x]])
            dfs(y+1, x, visited, curr.children[board[y][x]])
            dfs(y, x-1, visited, curr.children[board[y][x]])
            dfs(y, x+1, visited, curr.children[board[y][x]])
            visited[y][x] = 0
        # iterate the borad
        for i in range(height):
            for j in range(width):
                dfs(i, j, visited, trie)        
        return list(ret)