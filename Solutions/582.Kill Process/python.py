class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        queue, ret = [kill], []
        hashmap = {}
        for ind,val in enumerate(ppid):
            if val not in hashmap:
                hashmap[val] = [pid[ind]]
            else:
                hashmap[val].append(pid[ind])
        while queue:
            curr = queue.pop(0)
            ret.append(curr)
            if curr not in hashmap: continue
            queue = queue + hashmap[curr]
        return ret
            
                
        