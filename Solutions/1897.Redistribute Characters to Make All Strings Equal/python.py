class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l = len(words)
        cnt = defaultdict(int)
        for word in words:
            for char in word:
                cnt[char] += 1
        for char, val in cnt.items():
            if val % l != 0:    return False
        return True