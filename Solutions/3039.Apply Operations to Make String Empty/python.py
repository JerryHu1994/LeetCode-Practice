class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cnt = Counter(s)
        max_freq = max([cnt[k] for k in cnt])
        max_char = set([f for f in cnt if cnt[f] == max_freq])
        res = []
        for char in s:
            if char in max_char:    cnt[char] -= 1
            if cnt[char] == 0:  res.append(char)
        return "".join(res)