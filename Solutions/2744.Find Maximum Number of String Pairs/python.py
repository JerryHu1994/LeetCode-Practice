class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s, ret = set(), 0
        for w in words:
            if w[::-1] in s:
                ret += 1
            else:
                s.add(w)
        return ret