class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.idx = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.idx += 1
        while len(self.stack) and price >= self.stack[-1][0]:
            self.stack.pop()
        if len(self.stack) == 0:
            ret = self.idx
        else:
            ret = self.idx - self.stack[-1][1]
        self.stack.append([price, self.idx])
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)