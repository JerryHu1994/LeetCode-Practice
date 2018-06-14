class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dic = {}
        for i in wall:
            currlen = 0
            for j in range(0,len(i)-1):
                currlen += i[j]
                if currlen in dic:
                    dic[currlen] += 1
                else:
                    dic[currlen] = 1
        if len(dic) == 0:
            return len(wall)
        print dic
        bestkey, bestval = sorted(dic.iteritems(), key=lambda (k,v) : (-v,k))[0]
        return len(wall) - bestval