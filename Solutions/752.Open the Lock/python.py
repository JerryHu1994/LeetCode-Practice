class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadset = set([tuple([int(i) for i in s])   for s in deadends])
        queue, visited = [[0,0,0,0,0]], set((0,0,0,0))
        while len(queue):
            curr = queue.pop(0)
            currstate, currstep = curr[0:4], curr[4]
            strrep = "".join([str(i) for i in currstate])
            if tuple(currstate) in deadset: continue
            if strrep == target:  return currstep
            currstate_list = list(currstate)
            for i in xrange(4):
                #increment
                inc = currstate_list[:]
                inc[i] = (inc[i]+1)%10
                if tuple(inc) not in visited and tuple(inc) not in deadset:
                    visited.add(tuple(inc))
                    queue.append(inc+[currstep+1])
                #decrement
                dec = currstate_list[:]
                dec[i] = (dec[i]-1)%10
                if tuple(dec) not in visited and tuple(inc) not in deadset:
                    visited.add(tuple(dec))
                    queue.append(dec+[currstep+1])
        return -1