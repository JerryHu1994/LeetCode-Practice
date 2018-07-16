class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_list = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.hit_list.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while len(self.hit_list) != 0 and timestamp - self.hit_list[0] >= 300:
            # exceeds 5 minutes
            self.hit_list.pop(0) 
        return len(self.hit_list)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)