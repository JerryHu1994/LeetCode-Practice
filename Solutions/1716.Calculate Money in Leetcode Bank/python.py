class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            mod = 7 if i%7 == 0 else i%7
            div = int((i-1)/7)
            res += mod + div
        return res