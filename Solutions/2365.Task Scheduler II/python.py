class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        last_task = {}
        for task in tasks:
            if task not in last_task:
                day += 1
                last_task[task] = day
            else:
                if last_task[task] + space >= day:
                    day = last_task[task] + space + 1
                    last_task[task] = last_task[task] + space + 1
                else:
                    day += 1
                    last_task[task] = day
        return day