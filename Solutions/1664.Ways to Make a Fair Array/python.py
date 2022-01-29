class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        culsum = [0]*n
        for i in range(n-1, -1, -1):
            if i+2 >= n:
                culsum[i] = nums[i]
            else:
                culsum[i] = culsum[i+2] + nums[i]
        ans = 0
        evensum, oddsum = 0, 0
        for i in range(n):
            nextsum = culsum[i+1] if i+1 < n else 0
            nextnextsum = culsum[i+2] if i+2 < n else 0
            if i%2 == 0:
                if evensum + nextsum == oddsum + nextnextsum:
                    ans += 1
                evensum += nums[i]
            else:
                if evensum + nextnextsum == oddsum + nextsum:
                    ans += 1
                oddsum += nums[i]
        return ans