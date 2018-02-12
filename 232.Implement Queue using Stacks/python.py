class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pusharr = []
        self.poparr = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.pusharr.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.poparr)==0:
            while len(self.pusharr):
                self.poparr.append(self.pusharr.pop())
        return self.poparr.pop()
            

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.poparr)==0:
            while len(self.pusharr):
                self.poparr.append(self.pusharr.pop())
        return self.poparr[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.poparr)==0 and len(self.pusharr)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()