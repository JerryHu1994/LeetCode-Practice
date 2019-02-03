class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = collections.deque()
        ret = []
        for i in range(len(nums)):
            # remove all smaller element from the end
            while len(q) and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i-q[0]==k:# when the windows is full, pop the front out
                q.popleft()
            if i >= k-1: # when i is >= k-1, we need to append a max each time
                ret.append(nums[q[0]]) # q[0] will always store the max number for current interval
        return ret