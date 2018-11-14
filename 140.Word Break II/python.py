class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.mem = collections.defaultdict(list)
        wordlen, wordset = set([len(w) for w in wordDict]), set(wordDict)
        def helper(start):
            if start == len(s): return [""]
            if start in self.mem:   return self.mem[start]
            currlist = []
            for l in wordlen:
                if s[start:start+l] in wordset:
                    retlist = helper(start+l)
                    for string in retlist:  currlist.append(s[start:start+l]+" "+string if string != "" else s[start:start+l])
            self.mem[start] = currlist
            return currlist
        helper(0)
        return self.mem[0]