class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ans = 0
        dic = defaultdict(int)
        if k > len(s):  return ans
        for i in range(k):
            dic[s[i]] += 1
        if len(dic) == k:   ans += 1
        for i in range(k, len(s)):
            dic[s[i-k]] -= 1
            if dic[s[i-k]] == 0:    del dic[s[i-k]]
            dic[s[i]] += 1
            if len(dic) == k:   ans += 1
        return ans