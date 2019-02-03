class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:   return ""
        pos = bisect.bisect_right(self.store[key], (timestamp, chr(127)))
        return "" if pos == 0 else self.store[key][pos-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)