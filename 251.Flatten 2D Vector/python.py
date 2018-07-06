class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.ds = vec2d
        self.y = 0
        self.x = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.ds[self.y][self.x]
        self.x += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.y < len(self.ds):
            if self.x < len(self.ds[self.y]):
                return True
            self.y += 1
            self.x = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())