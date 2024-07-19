class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evenlist, oddlist, n = [], [], len(nums)
        for ind,val in enumerate(nums):
            if ind%2 == 1:
                oddlist.append(val)
            else:
                evenlist.append(val)
        evenlist.sort()
        oddlist.sort(reverse=True)
        ans = []
        ind,evenind, oddind = 0, 0, 0
        while ind < n:
            if ind%2 == 1:
                ans.append(oddlist[oddind])
                oddind += 1
            else:
                ans.append(evenlist[evenind])
                evenind += 1
            ind += 1
        return ans