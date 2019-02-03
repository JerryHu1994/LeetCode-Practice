class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.xc = x_center
        self.yc = y_center
        self.r = radius

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x = random.uniform(-self.r, self.r)
            y = random.uniform(-self.r, self.r)
            if x**2 + y**2 <= self.r**2:
                return [self.xc+x, self.yc+y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()