class Node(object):
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left, self.right = None, None
        
    def insert(self, n):
        if self.s >= n.e:
            # search for left tree
            if self.left == None:
                self.left = n
                return True
            return self.left.insert(n)
        elif self.e <= n.s:
            # search for right tree
            if self.right == None:
                self.right = n
                return True
            return self.right.insert(n)
        else:
            return False

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)