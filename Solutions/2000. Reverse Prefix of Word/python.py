class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = 0
        while ind < len(word):
            if word[ind] == ch: break
            ind += 1
        return word[0:ind+1][::-1] + word[ind+1:] if ind != len(word) else word