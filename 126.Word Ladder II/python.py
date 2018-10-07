class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        graph = collections.defaultdict(list)
        cnt, queue, found, step = collections.defaultdict(int), [beginWord], False, 0
        cnt[beginWord] = 1
        if beginWord in wordList:   wordList.remove(beginWord)
        if endWord in wordList:
            wordList.remove(endWord)
        else:
            return []
        while len(queue) and not found:
            step += 1
            l = len(queue)
            for k in range(l):
                currword = queue.pop(0)
                for i in range(len(currword)):
                    for j in range(ord('a'), ord('z')+1):
                        if chr(j) == currword[i]:   continue
                        nextword = currword[:i] + chr(j) + currword[i+1:]
                        if nextword == endWord:
                            found = True
                            graph[nextword].append(currword)
                        else:
                            if nextword in cnt and step < cnt[nextword]:
                                graph[nextword].append(currword)
                        if nextword not in wordList:    continue
                        wordList.remove(nextword)
                        queue.append(nextword)
                        cnt[nextword] = cnt[currword] + 1
                        graph[nextword].append(currword)
        # dfs to form the output
        self.ret = []
        def dfs(stack, end, dic):
            curr = stack[-1]
            if curr == end:
                self.ret.append(stack[::-1])
                return
            for w in dic[curr]: dfs(stack+[w], end, dic)
        dfs([endWord], beginWord, graph)
        return self.ret