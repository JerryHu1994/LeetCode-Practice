class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.intervals = []
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        if len(self.intervals) == 0:
            self.intervals.append(0)
            return 0
        currmax, currpair, maxidx = -1, None, 0
        for i in range(0, len(self.intervals) - 1):
            if self.intervals[i+1] - self.intervals[i] == 1:
                continue
            else:
                if (self.intervals[i+1] - self.intervals[i])//2 > currmax:
                    currmax = (self.intervals[i+1] - self.intervals[i])//2
                    currpair = [self.intervals[i], self.intervals[i+1]]
                    maxidx = i+1
        #check back
        if self.N-1 not in self.intervals:
            if self.N-1 - self.intervals[-1] > currmax:
                currmax = self.N-1 - self.intervals[-1]
                currpair = [self.N-1]
                maxidx = len(self.intervals)
        # check front
        if 0 not in self.intervals:
            if self.intervals[0] - 0 >= currmax:
                currmax = self.intervals[0] - 0
                currpair = [0]
                maxidx = 0
        
        if len(currpair) == 2:
            ret = (currpair[0] + currpair[1])//2
        else:
            ret = currpair[0]
        self.intervals.insert(maxidx, ret)
        return ret

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.intervals.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)