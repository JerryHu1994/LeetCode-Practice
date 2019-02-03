class Solution(object):
    def calOverlap(self, a, b):
            retstr, bestlen, l1, l2 = '', 0, len(a), len(b)
            for i in xrange(1, min(l1, l2)+1):
                if a[-i:] == b[:i]:
                    if bestlen < i:
                        bestlen = i
                        retstr = a+b[i:]
                if b[-i:] == a[:i]:
                    if bestlen < i:
                        bestlen = i
                        retstr = b+a[i:]
            return (retstr, bestlen) if bestlen > 0 else (a+b, 0)
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        setA = set(A)
        mem = {}
        while len(setA) > 1:
            bestlen, s = float('-inf'), None
            currx, curry = None, None
            for a, b in itertools.combinations(setA, 2):
                currstr, currlen = self.calOverlap(a, b) if (a,b) not in mem else mem[(a,b)]
                # store the result in cache
                if (a,b) not in mem:    mem[(a,b)] = currstr, currlen
                if currlen > bestlen:
                    bestlen = currlen
                    s = currstr
                    currx, curry = a, b
            setA.remove(currx)
            setA.remove(curry)
            setA.add(s)
        return setA.pop()