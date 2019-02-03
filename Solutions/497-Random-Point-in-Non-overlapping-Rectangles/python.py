class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.pts = []
        pre = 0
        for rect in rects:
            pre += (rect[2] - rect[0]+1)*(rect[3] - rect[1]+1)
            self.pts.append(pre)
        self.rects = rects

    def pick(self):
        """
        :rtype: List[int]
        """
        rand = random.randint(1, self.pts[-1])
        ind = bisect.bisect_left(self.pts, rand)
        x1,y1,x2,y2 = self.rects[ind]
        return [random.randint(x1,x2), random.randint(y1,y2)]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()