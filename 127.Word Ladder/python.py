class Solution(object):
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        ret = float("inf")
        wordList = set(wordList)
        queue = [(beginWord, 1)]
        while len(queue):
            currword, currtrans = queue.pop(0)
            if currword == endWord:
                ret = min(currtrans, ret)
                continue
            low, high = ord('a'), ord('z')+1
            for i in range(len(currword)):
                for j in range(low, high):
                    if chr(j) == currword[i]:   continue
                    tosearch = currword[:i] + chr(j) + currword[i+1:]
                    if tosearch in wordList:
                        wordList.remove(tosearch)
                        queue.append((tosearch, currtrans+1))
        return ret if ret != float("inf") else 0