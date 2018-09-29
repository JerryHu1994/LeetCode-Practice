class Node(object):
    def __init__(self):
        self.isword = False
        self.children = {}

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isword = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(root, word):
            curr = root
            for ind,c in enumerate(word):
                if c == ".":
                    for key,val in curr.children.iteritems():
                        if helper(val, word[ind+1:]):   return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    else:
                        curr = curr.children[c]
            return curr.isword
        return helper(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)