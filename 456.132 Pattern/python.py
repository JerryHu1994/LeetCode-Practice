class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:   return False
        min_arr = [nums[0]]
        for i in range(1,len(nums)):
            min_arr.append(min(min_arr[-1], nums[i]))
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if len(stack) == 0 or nums[i] <= stack[-1]:
                stack.append(nums[i])
                continue
            if nums[i] > min_arr[i]:
                while len(stack) > 0 and stack[-1] < nums[i]:
                    curr = stack.pop()
                    if curr > min_arr[i]:
                        print curr, nums[i], i
                        return True
                stack.append(nums[i])
        return False