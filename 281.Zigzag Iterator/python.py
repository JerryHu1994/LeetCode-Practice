class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.curr = 0
        self.lists = [v1, v2]

    def next(self):
        """
        :rtype: int
        """
        ret = self.lists[self.curr].pop(0)
        self.curr = (self.curr+1)%len(self.lists)
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        count = 0
        while len(self.lists[self.curr]) == 0:
            if count == len(self.lists):   return False
            self.curr = (self.curr+1)%len(self.lists)
            count += 1
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())