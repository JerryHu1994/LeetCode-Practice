class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.map = {}
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        currpair = (i,j)
        if currpair in self.map:
            return self.map[currpair]
        else:
            currsum = sum(self.nums[i:j+1])
            self.map[currpair] = currsum
            return currsum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)