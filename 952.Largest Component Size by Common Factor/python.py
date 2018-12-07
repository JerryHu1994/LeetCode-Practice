class DSU:
    def __init__(self, l):
        self.parents = [i for i in range(l)]
        self.ranks = [0]*l

    # outputs a unique id for x with path compression
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    # connects x and y together with union-by-rank
    def union(self, x, y):
        xid, yid = self.find(x), self.find(y)
        if xid == yid: # duplicate edge
            return False
        elif self.ranks[xid] < self.ranks[yid]:
            self.parents[xid] = yid
        elif self.ranks[xid] > self.ranks[yid]:
            self.parents[yid] = xid
        else:
            self.parents[yid] = xid
            self.ranks[xid] += 1
        return True

class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        li = []
        for num in A:
            factors, div = [], 2
            while div*div <= num:
                if num % div == 0:
                    while num%div == 0:
                        num /= div
                    factors.append(div)
                div += 1
            if not factors or num > 1:  factors.append(num)
            li.append(factors)
        primes = list({i for facs in li for i in facs}) # all primes
        prime_ind = {p:i for i, p in enumerate(primes)} # all primes to index
        dsu = DSU(len(primes))
        for facs in li:
            for x in facs:
                dsu.union(prime_ind[facs[0]], prime_ind[x])
        count = collections.Counter(dsu.find(prime_ind[facs[0]]) for facs in li)
        return max(count.values())