class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.stringidx = []

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.stringdic = collections.defaultdict(int)
        self.root = TrieNode()
        self.currinput = ""
        pairs = [[sentences[i], times[i]]  for i in range(len(sentences))]
        pairs = sorted(pairs, key = lambda x:[-x[1], x[0]])
        for ind, p in enumerate(pairs):
            curr = self.root
            word, freq = p[0], p[1]
            self.stringdic[word] = freq
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                    curr = curr.children[c]
                    curr.stringidx.append(word)
                else:
                    curr = curr.children[c]
                    if len(curr.stringidx) < 3:
                        curr.stringidx.append(word)
                    
    def helper(self, string):
        curr = self.root
        for c in string:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                return []
        return curr.stringidx

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != "#":
            self.currinput += c
            return self.helper(self.currinput)
        else:
            # end the input
            self.stringdic[self.currinput] += 1
            # increment the stringidx if necessary
            curr = self.root
            for c in self.currinput:
                curr = curr.children[c]
                currstrs = [[s, self.stringdic[s]]  for s in curr.stringidx]
                if [self.currinput, self.stringdic[self.currinput]] not in currstrs:
                    currstrs.append([self.currinput, self.stringdic[self.currinput]])
                currstrs = sorted(currstrs, key = lambda x : [-x[1], x[0]])
                sortedpairs = currstrs[:3] if len(currstrs) >=3 else currstrs
                curr.stringidx = [p[0]  for p in sortedpairs]
            self.currinput = ""
            return []
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)