class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a, count_b = s.count('a'), 0
        ans = len(s)
        for i in s:
            if i == 'a':
                count_a -= 1
                ans = min(ans, count_a + count_b)
            else:
                ans = min(ans, count_a + count_b)
                count_b += 1
        return ans