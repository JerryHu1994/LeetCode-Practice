class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.cols = n_cols
        self.rows = n_rows
        self.visited = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        while True:
            rand = random.randint(0, self.cols*self.rows-1)
            if rand not in self.visited:  
                self.visited.add(rand)
                return [rand/self.cols, rand%self.cols]
        

    def reset(self):
        """
        :rtype: void
        """
        self.visited = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()