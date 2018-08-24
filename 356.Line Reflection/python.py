class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points)==0:  return True
        max_x, min_x = max(p[0] for p in points), min(p[0] for p in points)
        axis = float((max_x+min_x))/2
        pos_dic = collections.defaultdict(set)
        for p in points:
            pos_dic[p[0]].add(p[1])
        for p in points:
            if p[1] not in pos_dic[axis+(axis-p[0])]:
                return False
        return True