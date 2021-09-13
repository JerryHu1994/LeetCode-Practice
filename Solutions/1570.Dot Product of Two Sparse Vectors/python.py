class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        for ind, val in enumerate(nums):
            if (val != 0):  self.dic[ind] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for ind, val in self.dic.items():
            if ind in vec.dic:
                ans += val*vec.dic[ind]
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)