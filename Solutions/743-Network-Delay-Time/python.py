class Solution(object):

    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for time in times:
            dic[time[0]].append((time[1], time[2]))
        delays = {K:0}        
        queue, cnt = [K], N
        while len(queue):
            curr = queue.pop(0)
            curr_neighbors = dic[curr]
            for nei in curr_neighbors:
                nextnode, nextdelay = nei[0], nei[1]
                if nextnode not in delays or delays[nextnode] > delays[curr] + nextdelay:
                    delays[nextnode] = delays[curr] + nextdelay
                    queue.append(nextnode)
        if len(delays.keys()) != N: return -1
        return max(delays.values())
                
                