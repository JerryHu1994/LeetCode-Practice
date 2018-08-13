class MyCalendarTwo(object):

    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlap:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlap.append([max(start,i), min(end, j)])
        self.calendar.append([start, end])
        return True        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)