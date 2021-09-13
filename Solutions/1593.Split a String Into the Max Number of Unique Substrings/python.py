class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def search(s:str) -> int:
            if len(s) == 0: return 0
            max_splits = 0
            for i in range(1,len(s)+1):
                first, second = s[0:i], s[i:]
                if first in seen:   continue
                seen.add(first)
                res = search(second) + 1
                max_splits = max(max_splits, res)
                seen.remove(first)
            return max_splits
        return search(s)