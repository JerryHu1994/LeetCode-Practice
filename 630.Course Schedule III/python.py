class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        sorted_course = sorted(courses, key = lambda x: [x[1], x[0]])
        pq, currtime = [], 0
        for c in sorted_course:
            heapq.heappush(pq, -c[0])
            currtime += c[0]
            if currtime > c[1]:
                currtime -= -heapq.heappop(pq)
        return len(pq)