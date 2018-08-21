class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.head = None
        self.tail = None
        self.queue = [None]*k
        self.cap = k
        self.currsize = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.currsize == self.cap:
            return False
        if self.currsize == 0:
            self.head = 0 
            self.tail = 0
            self.queue[0] = value
        else:
            if self.head == 0:
                self.head = self.cap-1
            else:
                self.head -= 1
            self.queue[self.head] = value
        self.currsize += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.currsize == self.cap:
            return False
        if self.currsize == 0:
            self.head = 0 
            self.tail = 0
            self.queue[0] = value
        else:
            self.tail = (self.tail+1)%self.cap
            self.queue[self.tail] = value
        self.currsize += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.currsize == 0:  return False
        self.queue[self.head] = None
        if self.currsize == 1:
            self.head = None
            self.tail = None
        else:
            self.head = (self.head+1)%self.cap
        self.currsize -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.currsize == 0:  return False
        self.queue[self.tail] = None
        if self.currsize == 1:
            self.head = None
            self.tail = None
        else:
            if self.tail == 0:
                self.tail = self.cap-1
            else:
                self.tail -= 1
        self.currsize -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():  return -1
        return self.queue[self.head]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():  return -1
        return self.queue[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.currsize == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.currsize == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()