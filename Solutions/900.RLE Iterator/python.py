class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.li = A

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(self.li) == 0:   return -1
        cnt = n
        while cnt > 0:
            if len(self.li) == 0:   return -1
            if cnt <= self.li[0]:
                ret = self.li[1]
                self.li[0] -= cnt
                return ret
            else:
                cnt -= self.li[0]
                self.li.pop(0)
                self.li.pop(0)
        return -1
            
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)