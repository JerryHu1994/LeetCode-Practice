class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = sorted(people, key = lambda x: [-x[0], x[1]])
        ret = []
        for p in sorted_people:
            ret.insert(p[1], p)
        return ret