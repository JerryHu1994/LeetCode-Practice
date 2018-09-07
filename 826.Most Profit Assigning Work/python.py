class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        task = zip(difficulty, profit)
        sort = sorted(task, key = lambda x:[x[0], x[1]])
        taskidx, ret, currbest = 0, 0, 0
        worker = sorted(worker)
        for i in range(len(worker)):
            while taskidx < len(sort) and sort[taskidx][0] <= worker[i]:
                currbest = max(currbest, sort[taskidx][1])
                taskidx += 1
            ret += currbest
        return ret