class MyCalendarThree(object):

    def __init__(self):
        self.dic = collections.defaultdict(int)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.dic[start] += 1
        self.dic[end] -= 1
        keys = sorted(self.dic.keys())
        curr, ret = 0, 0
        for k in keys:
            curr += self.dic[k]
            ret = max(curr, ret)
        return ret


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)