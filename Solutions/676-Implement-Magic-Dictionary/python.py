class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.s.add(i)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            for j in range(ord('a'), ord('z')+1):
                if word[i] == unichr(j):    continue
                newword = word[:i] + unichr(j) + word[i+1:]
                if newword in self.s:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)