class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.size += 1
        
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(self.size-1):
            self.queue.append(self.queue.pop(0))
        self.size -= 1
        return self.queue.pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for i in range(self.size-1):
            self.queue.append(self.queue.pop(0))
        ret = self.queue.pop(0)
        self.queue.append(ret)
        return ret

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()