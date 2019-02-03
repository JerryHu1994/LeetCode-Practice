class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack, ret = [-1], 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                idx = stack.pop()
                ret = max(ret, (i-stack[-1]-1)*heights[idx])
            stack.append(i)
        while stack[-1] != -1:
            idx = stack.pop()
            ret = max(ret, (len(heights) - stack[-1] - 1)*heights[idx])
        return ret