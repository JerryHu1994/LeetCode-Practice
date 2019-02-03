class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [-1] * len(nums)
        stack = []
        # first iteration
        for i in range(len(nums)):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) != 0 and nums[i] > nums[stack[-1]]:
                    last = stack.pop()
                    ret[last] = nums[i]
                stack.append(i)
        # second iteration
        for i in range(len(nums)):
            if len(stack) == 0: return ret
            # find the first element smaller that i, mark all elements after
            for j in range(len(stack)):
                if nums[i] > nums[stack[j]]:
                    elements_to_pop = len(stack) - j
                    for k in range(elements_to_pop):
                        ret[stack.pop()] = nums[i]
                    break
        return ret            
            