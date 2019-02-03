class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0:  return 0
        sorted_points = sorted(points, key = lambda x: [x[1], x[0]])
        ret = 1
        curr_arr = sorted_points[0][1]
        for i in range(1,len(sorted_points)):
            if sorted_points[i][0] <= curr_arr:
                # can shot this one
                continue
            else:
                curr_arr = sorted_points[i][1]
                ret += 1
        return ret
            
                