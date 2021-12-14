class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        curr_cnt = defaultdict(int)
        ans = 0
        for char in s:
            ans += counter[char]
            counter[char] -= 1
        return ans