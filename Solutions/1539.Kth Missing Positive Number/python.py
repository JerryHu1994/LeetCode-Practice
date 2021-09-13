class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr, ind = 1, 0
        while ind < len(arr):
            if curr != arr[ind]:
                k -= 1
                if k == 0:  return curr
            else:
                ind += 1
            curr += 1
        curr -= 1
        for i in range(k):
            curr += 1
        return curr