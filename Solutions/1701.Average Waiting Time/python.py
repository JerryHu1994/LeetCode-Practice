class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        currtime = 0
        total_wait = 0
        for (arrivetime, preparetime) in customers:
            if currtime <= arrivetime:
                currtime = arrivetime + preparetime
                total_wait += preparetime
            else:
                total_wait += currtime - arrivetime + preparetime
                currtime = currtime + preparetime
        return total_wait/len(customers)