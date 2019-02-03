Trie = lambda: collections.defaultdict(Trie)
wordidx = "word"
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        for weight, word in enumerate(words):
            post = "#"+word
            for i in range(len(word), -1, -1):
                curr = self.trie
                for c in word[i:]:
                    curr = curr[c]
                for c in post:
                    curr = curr[c]
                    if wordidx not in curr or curr[wordidx] < weight:
                        curr[wordidx] = weight

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        complete = suffix+"#"+prefix
        curr = self.trie
        for c in complete:
            if c not in curr:
                return -1
            curr = curr[c]
        if wordidx not in curr: return -1
        return curr[wordidx]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)