class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        time = [0]*len(flowers)
        for t, pos in enumerate(flowers):
            time[pos-1] = t+1
        pos = 0
        ret = float("inf")
        while pos + k + 1 < len(time):
            limit = max(time[pos], time[pos+k+1])
            check = True
            for i in xrange(0, k):
                if time[pos+i+1] < limit:
                    check = False
                    break
            if check:
                ret = min(limit, ret)
            pos += 1
        return -1 if ret == float("inf") else ret
                    
                