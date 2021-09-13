class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word_list = text.split()
        s = set()
        for char in brokenLetters:  s.add(char)
        ans = 0
        for word in word_list:
            cantype = True
            for c in word:
                if c in s:
                    cantype = False
                    break
            if cantype: ans += 1
        return ans