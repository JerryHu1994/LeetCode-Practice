class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dic = collections.defaultdict(list)
        for ind, val in enumerate(nums):
            self.dic[val].append(ind)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ran = random.randint(0, len(self.dic[target])-1)
        return self.dic[target][ran]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)