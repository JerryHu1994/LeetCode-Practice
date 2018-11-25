# O(n) solution
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = -1, -1
        currsum, ret = 0, float("inf")
        while True:
            if currsum < s:
                # move right
                right += 1
                if right>= len(nums): break
                currsum += nums[right]
            else:
                # move left
                left += 1
                currsum -= nums[left]
            if currsum >= s:
                ret = min(right-left, ret)
        
        return 0 if ret == float("inf") else ret

# O(nlogn) solution
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        culsum, curr = [0], 0
        for n in nums:
            curr += n
            culsum.append(curr)
        ret = float("inf")
        for start in range(len(nums)):
            ind = bisect.bisect_left(culsum[start:], culsum[start]+s)
            if ind < len(culsum[start:]):
                ret = min(ret, ind)
        return ret if ret != float("inf") else 0