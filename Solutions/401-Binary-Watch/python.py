class Solution(object):
    def helper(self, on, total):
        if on > total:
            return None
        if on == total:
            return ["1"*on]
        if on == 0:
            return ["0"*total]
        curron = self.helper(on-1, total-1)
        curroff = self.helper(on, total-1)
        ret = []
        if curron != None:
            for i in curron:    ret.append("1"+i)
        if curroff != None:
            for i in curroff:    ret.append("0"+i)
        return ret
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        hour = 0
        times = self.helper(num, 10)
        for t in times:
            h, m = int(t[0:4], 2), int(t[4:10], 2)
            if h >= 12 or m >= 60:
                continue
            else:
                mtext = str(m) if m >= 10 else "0"+str(m)
                ret.append(str(h) + ":" + mtext)
        return ret