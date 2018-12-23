class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        l = len(words[0])
        if l == 1:
            return [[w] for w in words]
        trie = collections.defaultdict(list)
        for w in words:
            for i in range(1, len(w)+1):
                trie[w[:i]].append(w)
        ans = []
        def dfs(prelist, prefix):
            if len(trie[prefix]) == 0:  return
            for nextstr in trie[prefix]:
                nextlist = prelist+[nextstr]
                if len(nextlist) == l:
                    ans.append(nextlist)
                    continue
                nextprefix = "".join([w[len(nextlist)]   for w in nextlist])
                dfs(nextlist, nextprefix)
        for w in words: dfs([w], w[1])
        return ans