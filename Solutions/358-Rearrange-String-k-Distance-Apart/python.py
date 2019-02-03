from heapq import *
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:  return s
        counter = collections.Counter(s)
        pq = []
        for key, val in counter.items():
            heappush(pq,[-val, key])
        ret = []
        slen = len(s)
        while len(pq):
            currlist = []
            l = min(slen, k)
            for i in range(l):
                if len(pq) == 0:
                    return ""
                #print pq
                curr = heappop(pq)
                ret.append(curr[1])
                curr[0]+=1
                if curr[0] < 0:
                    currlist.append(curr)
                slen-=1
            # append currlist back to pq
            for c in currlist:
                heappush(pq, c)
        return "".join(ret)
                