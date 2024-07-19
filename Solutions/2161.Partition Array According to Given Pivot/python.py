class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smallq, largeq, pivot_count = [], [], 0
        for n in nums:
            if n < pivot:
                smallq.append(n)
            elif n > pivot:
                largeq.append(n)
            else:
                pivot_count += 1
        return smallq + [pivot]*pivot_count + largeq