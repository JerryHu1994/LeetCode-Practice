class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0]*(self.n*2)
        # build the segment tree
        i, j = self.n, 0
        while i < 2*self.n:
            self.tree[i] = nums[j]
            i += 1
            j += 1
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += self.n
        self.tree[i] = val
        while i > 0:
            left = right = i
            if i%2 == 0:
                right = i+1
            else:
                left = i-1
            self.tree[i//2] = self.tree[left] + self.tree[right]
            i //= 2

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        left, right = i+self.n, j+self.n
        ans = 0
        while left <= right:
            # check if left is the right child of parent
            if left%2:
                ans += self.tree[left]
                left += 1
            # check if right is the left child of parent
            if right%2 == 0:
                ans += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)