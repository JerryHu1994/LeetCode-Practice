class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        # perform BFS
        ans = 0
        queue = [curr]
        while len(queue) > 0:
            currnode = queue.pop(0)
            ans += currnode.count
            queue += list(currnode.children.values())
        return ans
        
    def erase(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return
            curr = curr.children[char]
        if curr.count > 0:
            curr.count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)