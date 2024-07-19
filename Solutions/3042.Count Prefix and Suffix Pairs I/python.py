class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(worda: str, wordb: str):
            if len(worda) > len(wordb): return False
            for ind, char in enumerate(worda):
                if char != wordb[ind]:  return False
            for ind, char in enumerate(worda[::-1]):
                if char != wordb[::-1][ind]:    return False
            return True
        res = 0
        for ind, w in enumerate(words):
            for j in range(ind+1, len(words)):
                if isPrefixAndSuffix(w, words[j]):  res += 1
        return res