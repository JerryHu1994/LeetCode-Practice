class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) > 0:
            n = len(nums)
            self.n = n
            self.tree = [0]*(n*2)
            # build the tree
            i, j = n, 0
            while i < 2*n:
                self.tree[i] = nums[j]
                i += 1
                j += 1
            for i in range(n-1, 0, -1):
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
        s = 0
        while left <= right:
            if left%2:
                s += self.tree[left]
                left +=1
            if right%2 == 0:
                s += self.tree[right]
                right -=1
            left //= 2
            right //= 2
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)