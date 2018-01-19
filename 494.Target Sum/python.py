
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        summap = collections.defaultdict(int)
        summap[0] = 1
        for x in nums:
            curr = collections.defaultdict(int)
            for y in summap:
                curr[y+x] += summap[y]
                curr[y-x] += summap[y]
            summap = curr
        return summap[S]