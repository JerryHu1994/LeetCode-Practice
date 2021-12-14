class Solution:
    def secondHighest(self, s: str) -> int:
        first, second = -1, -1
        for i in s:
            if i.isdigit():
                num = int(i)
                if num > first:
                    second = first
                    first = num
                elif num < first and num > second:
                    second = num
        return second if first != second else -1