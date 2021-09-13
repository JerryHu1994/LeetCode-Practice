class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        nstr = str(n)
        ind = len(nstr) - 1
        while len(nstr) > 0:
            res.append(nstr[-3:])
            nstr = nstr[:-3]
        return ".".join(res[::-1])