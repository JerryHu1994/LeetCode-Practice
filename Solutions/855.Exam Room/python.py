class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.hq = [(self.dis(-1, N), -1, N)]
        self.N = N

    # calculates the distance between two points
    def dis(self, left, right):
        if left == -1:
            return -right
        elif right == self.N:
            return -(self.N - 1 - left)
        else:
            return -(abs(right-left)//2)
        
    def seat(self):
        """
        :rtype: int
        """
        currdis, start, end = heapq.heappop(self.hq)
        if start == -1:
            seat = 0
        elif end == self.N:
            seat = self.N - 1
        else:
            seat = (start+end)//2
        heapq.heappush(self.hq, (self.dis(start, seat), start, seat))
        heapq.heappush(self.hq, (self.dis(seat, end), seat, end))
        return seat

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        pre_int, next_int = None, None
        for interval in self.hq:
            if interval[2] == p:
                pre_int = interval
            elif interval[1] == p:
                next_int = interval
            if pre_int and next_int:   break
        self.hq.remove(pre_int)
        self.hq.remove(next_int)
        heapq.heapify(self.hq)
        heapq.heappush(self.hq, (self.dis(pre_int[1], next_int[2]), pre_int[1], next_int[2]))


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)