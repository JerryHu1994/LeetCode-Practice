class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        
        def dfs(start, end, visited):
            if start == end:    return True
            for nextnode in graph[start]:
                if nextnode not in visited:
                    visited.add(nextnode)
                    ret = dfs(nextnode, end, visited)
                    if ret: return True
                    visited.remove(nextnode)
            return False
        equs, notequs = [e for e in equations if "==" in e], [e for e in equations if "!=" in e]
        for equ in equs:
            left, right = equ.split("==")
            graph[left].add(right)
            graph[right].add(left)
        for equ in notequs:
            left, right = equ.split("!=")
            ret = dfs(left, right, set([left]))
            if ret: return False
        return True