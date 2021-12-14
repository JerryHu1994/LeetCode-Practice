class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])
        for ind, val in enumerate(word):
            if val in vowel_set:
                ans += (ind+1)*(len(word)-ind)
        return ans