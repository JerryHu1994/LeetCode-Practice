class Solution:
    def minSwaps(self, s: str) -> int:
        closing_count = 0
        max_cnt = 0
        for i in s:
            if i == ']':
                closing_count += 1
            else:
                closing_count -= 1
            max_cnt = max(closing_count, max_cnt)
        return math.ceil(max_cnt/2)