class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)
        if len(s) < 3:  return 0
        for i in range(3):
            cnt[s[i]] += 1
        ans = 0
        if len(cnt) == 3:
            ans += 1
        for i in range(3, len(s)):
            cnt[s[i]] += 1
            cnt[s[i-3]] -= 1
            if cnt[s[i-3]] == 0: del cnt[s[i-3]]
            if len(cnt) == 3:
                ans += 1
        return ans