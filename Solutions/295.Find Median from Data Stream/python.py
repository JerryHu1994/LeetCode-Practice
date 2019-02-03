from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_pq = []
        self.right_pq = []
        self.l = 0
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.l += 1
        if len(self.right_pq) > len(self.left_pq):
            rightmin = heappop(self.right_pq)
            heappush(self.left_pq, -min(num, rightmin))
            heappush(self.right_pq, max(num, rightmin))
            return
        heappush(self.left_pq, -num)
        # we always keep right >= left
        heappush(self.right_pq, -heappop(self.left_pq))
        
    def findMedian(self):
        """
        :rtype: float
        """
        ret = None
        if self.l%2:
            ret = float(heappop(self.right_pq))
            heappush(self.right_pq, ret)
        else:
            l, r = -heappop(self.left_pq), heappop(self.right_pq)
            ret = (float(l) + float(r))/float(2)
            heappush(self.left_pq, -l)
            heappush(self.right_pq, r)
        return ret
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()