class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.currState = nums
        self.preState = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.currState = self.preState
        self.preState = list(self.preState)
        return self.currState

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = list(self.currState)
        for i in range(len(nums)):
            curridx = random.randint(0, len(nums)-1)
            self.currState[i] = nums.pop(curridx)
        return self.currState
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()