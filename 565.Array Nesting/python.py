class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        visited = [False]*l
        ret = 0
        for i in range(l):
            if visited[i]:  continue
            s = set([nums[i]])
            curr = nums[i]
            while True:
                visited[curr] = True
                nextnum = nums[curr]
                if nextnum not in s:
                    s.add(nextnum)
                else:
                    ret = max(ret, len(s))
                    break
                curr = nextnum
        return ret