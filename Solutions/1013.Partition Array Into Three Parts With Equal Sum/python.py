class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s, l = sum(A), len(A)
        if s%3: return False
        one_third = s/3
        cul = 0
        cnt = 0
        for i in A:
            cul += i
            if cul == one_third:
                cul = 0
                cnt += 1
        return cnt == 3