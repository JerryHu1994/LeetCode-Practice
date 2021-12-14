class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        prev = None
        ans = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = defaultdict(int)
        for ind, val in enumerate(word):
            if val not in vowels:
                count.clear()
                prev = None
            else:
                count[val] += 1
                if prev == None:
                    prev = ind
                copy_count = dict(count)
                temp_prev = prev
                while len(copy_count) == 5:
                    ans += 1
                    copy_count[word[temp_prev]] -= 1
                    if copy_count[word[temp_prev]] == 0: del copy_count[word[temp_prev]]
                    temp_prev += 1
        return ans
            