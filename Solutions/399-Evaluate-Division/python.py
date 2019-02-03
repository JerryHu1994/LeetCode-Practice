class Solution(object):
    def dfs(self, dic, fr, to, val, visited):
        ret = None
        if fr not in dic:   return False
        if fr == to: return 1.0
        for pair in dic[fr]:
            if pair[0] in visited:  continue
            if pair[0] == to:   return val*pair[1]
            else:
                visited.add(pair[0])
                ret = self.dfs(dic, pair[0], to, val*pair[1], visited)
                if ret != False:    return ret
                visited.remove(pair[0])
        return False if ret == None else ret 
    
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic = collections.defaultdict(list)
        for ind, equ in enumerate(equations):
            dic[equ[0]].append((equ[1], values[ind]))
            dic[equ[1]].append((equ[0], float(1)/values[ind]))
        ret = []
        for q in queries:
            res = self.dfs(dic, q[0], q[1], 1.0, set([q[0]]))
            if res == False:
                ret.append(-1.0)
            else:
                ret.append(res)
        return ret