class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n, 1):
                if j-i >= indexDifference and abs(nums[j]-nums[i]) >= valueDifference:
                    return [i, j]
        return [-1, -1]