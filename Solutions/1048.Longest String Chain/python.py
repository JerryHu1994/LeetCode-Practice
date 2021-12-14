class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordset = set(words)
        minlen = min([len(w)    for w in words])
        memset = {}
        ans = 0
        def dfs(currword):
            if len(currword) == minlen:
                memset[currword] = 1
                return 1
            currbest = 0
            for i in range(len(currword)):
                nextword = currword[:i] + currword[i+1:]
                if nextword in wordset:
                    if nextword in memset:
                        currbest = max(currbest, memset[nextword])
                    else:
                        res = dfs(nextword)
                        currbest = max(currbest, res)
            memset[currword] = currbest + 1
            return currbest + 1
        for w in words:
            ans = max(ans, dfs(w))
        return ans
                
            