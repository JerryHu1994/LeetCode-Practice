class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        l = [0]*26
        for i in tasks:
            l[ord(i) - ord("A")] += 1
        l.sort()
        intervals = l[25]-1
        maxidle = n*intervals
        for i in range(24, 0, -1):
            if i==0:
                break
            maxidle -= min(intervals, l[i])
        
        return len(tasks) if maxidle<=0 else maxidle+len(tasks)