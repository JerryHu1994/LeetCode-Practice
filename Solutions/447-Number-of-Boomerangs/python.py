class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        for i in range(len(points)):
            dis = collections.defaultdict(int)
            for j in range(len(points)):
                if j == i:  continue
                currdis = abs(points[i][0]-points[j][0])**2+abs(points[i][1]-points[j][1])**2
                dis[currdis] += 1
            for k, v in dis.iteritems():
                if v > 1:
                    ret += v*(v-1)
        return ret
                    
                    
                    
                    