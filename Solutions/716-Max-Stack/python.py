class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        currmax = x if len(self.stack2)==0 else max(self.stack2[-1], x)
        self.stack2.append(currmax)
        

    def pop(self):
        """
        :rtype: int
        """
        ret = self.stack1.pop()
        self.stack2.pop()
        return ret
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack2[-1]

    def popMax(self):
        """
        :rtype: int
        """
        temp = []
        currmax = self.stack2[-1]
        while self.stack1[-1] != currmax:
            temp.append(self.stack1.pop())
            self.stack2.pop()
        self.stack1.pop()
        self.stack2.pop()
        for i in temp[::-1]:
            nextmax = i if len(self.stack2)==0 else max(self.stack2[-1], i)
            self.stack1.append(i)
            self.stack2.append(nextmax)
        return currmax

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()