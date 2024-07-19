class Solution:
    def maxProduct(self, s: str) -> int:
        n, pali_dict = len(s), {}
        for mask in range(1, 1 << n): # different combinations
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali_dict[mask] = len(subseq)
        ans = 0
        for left_sub, left_len in pali_dict.items():
            for right_sub, right_len in pali_dict.items():
                if left_sub & right_sub == 0:
                    ans = max(ans, left_len*right_len)
        return ans