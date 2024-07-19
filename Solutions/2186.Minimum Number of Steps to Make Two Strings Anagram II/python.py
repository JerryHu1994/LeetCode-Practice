class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        ans = 0
        for key_s in cnt_s:
            value_s = cnt_s[key_s]
            value_t = cnt_t[key_s] if key_s in cnt_t else 0
            if value_s-value_t > 0:
                ans += value_s-value_t
        for key_t in cnt_t:
            value_t = cnt_t[key_t]
            value_s = cnt_s[key_t] if key_t in cnt_s else 0
            if value_t-value_s > 0:
                ans += value_t-value_s
        return ans
            