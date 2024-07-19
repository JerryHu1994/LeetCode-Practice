class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        charset = set()
        ans = set()
        for c in word:
            if c.isupper():
                if chr(ord(c)+32) in charset:
                    ans.add(ord(c)+32)
            else:
                charset.add(c)
        return len(ans)