class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        ts = self.getTimeStamp(timestamp, "Second", False)
        for ind, i in enumerate(self.logs):
            if i[1] > ts:
                self.logs.insert(ind, [id, ts])
                return
        self.logs.append([id, ts])
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        startts = self.getTimeStamp(s, gra, False)
        endts = self.getTimeStamp(e, gra, True)
        ret = []
        for i in self.logs:
            if i[1] >= startts and i[1] < endts:
                ret.append(i[0])
            if i[1] > endts:
                break
        return ret
        
        
    def getTimeStamp(self, timestr, gra, isEnd):
        times = [int(t) for t in timestr.split(":")]
        g = {"Year":1,"Month":2,"Day":3,"Hour":4,"Minute":5,"Second":6}
        ret = 0
        for i in range(g[gra]):
            if i == g[gra]-1 and isEnd:
                ret += (times[i]+1)*math.pow(10, 12-2*i)
            else:
                ret += times[i]*math.pow(10, 12-2*i)
        return ret
    
# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)