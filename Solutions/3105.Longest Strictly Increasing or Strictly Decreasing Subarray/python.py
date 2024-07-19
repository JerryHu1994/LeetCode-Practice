class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        currLen, positive = 0, True
        for i, n in enumerate(nums):
            if currLen == 0:
                currLen += 1
            else:
                if positive:
                    if n > nums[i-1]:
                        currLen += 1
                    elif n == nums[i-1]:
                        currLen = 1
                    else:
                        currLen = 2
                        positive = False
                else:
                    if n < nums[i-1]:
                        currLen += 1
                    elif n == nums[i-1]:
                        currLen = 1
                    else:
                        currLen = 2
                        positive = True
            ans = max(ans, currLen)
        return ans