class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        end = True
        for i, word in enumerate(words):
            # map each char in word to a Trie, in the end, set the end tire's True key to the word index
            reduce(dict.__getitem__, word, trie)[end] = i

        stack = trie.values()
        ret = ""
        while stack:
            curr = stack.pop()
            if end in curr: # found an word ending here
                word = words[curr[end]]
                if len(word) > len(ret) or (len(word) == len(ret) and word < ret):
                    ret = word
                stack.extend(curr[letter] for letter in curr if letter != end)
        return ret
            
            
                