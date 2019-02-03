class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set([w for w in wordList if len(w) == len(beginWord)])
        if endWord not in wordSet or len(beginWord) != len(endWord):    return []
        dic = {}
        res = []
        dic[beginWord] = [[beginWord]]
        end = False
        while len(dic) and not end:
            newdic = collections.defaultdict(list)
            for w in dic:
                if w == endWord:
                    res.extend(v for v in dic[w])
                    end = True
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            newword = w[:i]+c+w[i+1:]
                            if newword in wordSet:
                                newdic[newword] += [j+[newword] for j in dic[w]]
            wordSet -= set(newdic.keys())
            dic = newdic
        return res