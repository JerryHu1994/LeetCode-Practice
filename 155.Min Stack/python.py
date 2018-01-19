class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minval = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack)==0:
            self.stack.append(x)
            self.minval = x
        else:
            if x <= self.minval:
                self.stack.append(self.minval)
                self.minval = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        curr = self.stack.pop()
        if curr == self.minval:
            self.minval = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()