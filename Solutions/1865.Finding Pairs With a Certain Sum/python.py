class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = defaultdict(int)
        self.cnt2 = defaultdict(int)
        self.nums1 = nums1
        self.nums2 = nums2
        for n in nums1:  self.cnt1[n] += 1
        for n in nums2: self.cnt2[n] += 1

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.nums2[index] += val
        self.cnt2[old] -= 1
        self.cnt2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for k,v in self.cnt1.items():
            if tot-k in self.cnt2:
                ans += v*self.cnt2[tot-k]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)