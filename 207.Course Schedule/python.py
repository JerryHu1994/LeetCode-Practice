class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dic = collections.defaultdict(list)
        for e in prerequisites:
            dic[e[1]].append(e[0])
        for i in range(numCourses):
            stack, s = [i], set([i])
            while len(stack):
                curr = stack.pop()
                pres = dic[curr]
                for p in pres:
                    if p == i:  return False
                    if p not in s:
                        stack.append(p)
                        s.add(p)
        return True