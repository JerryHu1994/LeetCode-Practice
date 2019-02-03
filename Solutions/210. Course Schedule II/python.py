class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        dic2 = collections.defaultdict(list)
        for e in prerequisites:
            dic[e[0]].append(e[1])
            dic2[e[1]].append(e[0])
        degrees = [len(dic[i]) for i in range(numCourses)] # # of numbers the course is pointed
        zeros = [i for i in range(numCourses) if degrees[i] == 0]
        ret = []
        while zeros:
            temp = []
            ret += zeros[:]
            for z in zeros:
                for n in dic2[z]:
                    degrees[n] -= 1
                    if degrees[n] == 0:
                        temp.append(n)
            zeros = temp
        return [] if len(ret) != numCourses else ret