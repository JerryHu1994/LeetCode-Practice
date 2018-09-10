class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        # find the min distance nuts
        first_nut, best_dis, ret = None,  float("-inf"), 0
        for n in nuts:
            n_to_s = abs(n[0]-squirrel[0]) + abs(n[1]-squirrel[1])
            n_to_t = abs(n[0]-tree[0]) + abs(n[1]-tree[1])
            currsave = n_to_t - n_to_s
            if best_dis < currsave:
                best_dis = currsave
                first_nut = n
            ret += 2*n_to_t
        ret = ret - best_dis
        return ret