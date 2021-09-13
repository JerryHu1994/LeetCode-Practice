class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        sortlist = sorted([a,b,c])
        [l1, l2, l3] = sortlist
        if l1 + l2 > l3:
            return l3 + int((l1+l2-l3)/2)
        else:
            return l1+l2