class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        uppercase = defaultdict(int)
        for ind,c in enumerate(word):
            if c.isupper() and c not in uppercase:
                uppercase[c] = ind
        for ind,c in enumerate(word):
            if c.islower() and chr(ord(c)-32) in uppercase and ind > uppercase[chr(ord(c)-32)]:
                del uppercase[chr(ord(c)-32)]
        ans = set()
        for c in word:
            if c.islower() and c.upper() in uppercase:
                ans.add(c)
        return len(ans)
        