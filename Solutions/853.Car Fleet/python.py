class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [(position[i], speed[i])    for i in range(len(position))]
        pairs = sorted(pairs, key = lambda x:[x[0], x[1]])
        remain_times = []
        for p in pairs:
            remain_times.append(float(target-p[0])/float(p[1]))
        ret = 0
        while len(remain_times):
            curr_time = remain_times.pop()
            while len(remain_times):
                if remain_times[-1] <= curr_time:
                    remain_times.pop()
                else:
                    break
            ret += 1
        return ret